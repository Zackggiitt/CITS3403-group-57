from flask import render_template, url_for, redirect, request, jsonify, current_app, flash
from werkzeug.security import generate_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy import desc, String # Added for ordering
from sqlalchemy.sql import func
import json
from datetime import datetime, timezone, timedelta
import openai

from . import main_bp, db, models # Import blueprint, db, and models from app package (__init__.py)
from .forms import SignupForm, LoginForm, EditProfileForm

# --- Routes are now part of the main_bp blueprint ---

# Define route for the home page
@main_bp.route("/")
def index():
    return render_template("index.html", title='Home')

@main_bp.route("/chat_page") # Route for displaying the chat page
@login_required # Optional: if you want chat page to be login protected
def chat_page():
    return render_template("chat.html", title="Chat with FitPal AI")

# Define route for the login page
@main_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    error = None

    if request.method == "POST":
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        
        if not email or not password:
            error = "Email and password are required."
        else:
            user = models.User.query.filter_by(email=email).first()
            
            if user and user.check_password(password):
                if form.validate_on_submit(): 
                    login_user(user)
                    flash('Logged in successfully.')
                    next_page = request.args.get('next')
                    return redirect(next_page or url_for("main.profile"))
                else:
                    error = "Login failed due to form validation issues after credential check."
            else: 
                error = "Invalid email or password."

    return render_template("login.html", form=form, title="Login", error=error)

# Define route for the signup page
@main_bp.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    error = None

    if form.validate_on_submit():
        email = form.email.data
        
        existing_user = models.User.query.filter_by(email=email).first()
        if existing_user:
            error = "User already exists with that email."
            return render_template("signup.html", form=form, title="Sign Up", error=error)
        
        hashed_password = generate_password_hash(form.password.data)
        
        new_user = models.User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=email,
            password_hash=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        flash("Account created successfully! Please log in.")
        return redirect(url_for("main.login"))
    
    return render_template("signup.html", form=form, title="Sign Up", error=error)

# Define route for the posts page
@main_bp.route("/posts")
@login_required
def posts():
    my_plans_query = models.WorkoutPlan.query.filter_by(user_id=current_user.id)
    my_plan_entries = my_plans_query.all()
    my_plans_by_day = {day: [] for day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]}
    for entry in my_plan_entries:
        if entry.day_of_week in my_plans_by_day:
            my_plans_by_day[entry.day_of_week].append(entry.to_dict())
    
    ordered_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    ordered_my_plans_by_day = {day: my_plans_by_day.get(day, []) for day in ordered_days}

    latest_shared_times_subq = db.session.query(
        models.SharedPlan.sharer_id,
        func.max(models.SharedPlan.shared_at).label('latest_shared_at')
    ).filter(
        models.SharedPlan.recipient_id == current_user.id
    ).group_by(
        models.SharedPlan.sharer_id
    ).subquery('latest_shared_times_subq')

    latest_share_records_for_recipient = db.session.query(models.SharedPlan).join(
        latest_shared_times_subq,
        (models.SharedPlan.sharer_id == latest_shared_times_subq.c.sharer_id) &
        (models.SharedPlan.shared_at == latest_shared_times_subq.c.latest_shared_at)
    ).filter( 
        models.SharedPlan.recipient_id == current_user.id
    ).order_by(models.SharedPlan.sharer_id).all() 

    sharers_for_dropdown = []
    latest_plans_data_for_js = {}

    for share_record in latest_share_records_for_recipient:
        sharer_user = share_record.sharer 
        if not sharer_user: 
            continue 
        
        sharer_id = sharer_user.id
        sharer_display_name = f"{sharer_user.first_name} {sharer_user.last_name}"

        sharers_for_dropdown.append({
            'id': sharer_id,
            'display_text': f"Plan from {sharer_display_name}"
        })

        sharer_workout_entries = models.WorkoutPlan.query.filter_by(user_id=sharer_id).all()
        
        sharer_plans_by_day = {day: [] for day in ordered_days}
        has_plan_entries = False
        for entry in sharer_workout_entries:
            day_key = entry.day_of_week.lower()
            if day_key in sharer_plans_by_day:
                sharer_plans_by_day[day_key].append(entry.to_dict())
                has_plan_entries = True
        
        ordered_sharer_plans = {day: sharer_plans_by_day.get(day, []) for day in ordered_days}

        latest_plans_data_for_js[str(sharer_id)] = {
            'sharer_id': sharer_id,
            'sharer_name': sharer_display_name,
            'shared_at': share_record.shared_at.strftime('%Y-%m-%d %H:%M:%S'),
            'recipient_id': share_record.recipient_id,
            'plan_details': ordered_sharer_plans,
            'plan_exists': has_plan_entries
        }
        
    return render_template(
        "posts.html", 
        title="My Workout Week & Shared Plans", 
        my_plans_data=ordered_my_plans_by_day, 
        sharers_for_dropdown=sharers_for_dropdown,
        latest_plans_data_json=json.dumps(latest_plans_data_for_js)
    )

@main_bp.route("/profile")
@login_required
def profile():
    total_volume = db.session.query(
        func.sum(models.SavedWorkouts.sets * models.SavedWorkouts.reps * models.SavedWorkouts.weight)
    ).filter(
        models.SavedWorkouts.user_id == current_user.id
    ).scalar() or 0

    total_workouts = db.session.query(
    func.count(func.distinct(
        func.cast(models.SavedWorkouts.save_date, String) + models.SavedWorkouts.day_of_week
    ))
    ).filter(
        models.SavedWorkouts.user_id == current_user.id
    ).scalar() or 0

    return render_template(
        "profile.html", 
        title="Profile",
        total_volume=total_volume,
        total_workouts=total_workouts
    )

@main_bp.route("/edit_profile", methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.bio = form.bio.data
        current_user.bmr = form.bmr.data
        db.session.commit()
        flash('Your profile has been updated.')
        return redirect(url_for('main.profile'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.bio.data = current_user.bio
        form.bmr.data = current_user.bmr
    return render_template('edit_profile.html', title='Edit Profile', form=form)

@main_bp.route("/api/workout_history", methods=['GET'])
@login_required
def get_workout_history():
    try:
        five_weeks_ago = datetime.now(timezone.utc) - timedelta(weeks=5)
        
        saved_workouts = models.SavedWorkouts.query.filter(
            models.SavedWorkouts.user_id == current_user.id,
            models.SavedWorkouts.save_date >= five_weeks_ago
        ).order_by(models.SavedWorkouts.save_date).all()
        
        exercise_counts = {}
        for workout in saved_workouts:
            exercise_name = workout.exercise_name.lower()
            exercise_counts[exercise_name] = exercise_counts.get(exercise_name, 0) + 1
        
        top_exercises = sorted(exercise_counts.items(), key=lambda x: x[1], reverse=True)[:3]
        top_exercise_names = [exercise[0] for exercise in top_exercises]
        
        weekly_data = {}
        for workout in saved_workouts:
            workout_date = workout.save_date
            week_start = workout_date - timedelta(days=workout_date.weekday())
            week_key = week_start.strftime('%b %d')
            
            if week_key not in weekly_data:
                weekly_data[week_key] = {
                    'total_volume': 0
                }
                for exercise in top_exercise_names:
                    weekly_data[week_key][exercise] = []
            
            volume = workout.sets * workout.reps * workout.weight
            weekly_data[week_key]['total_volume'] += volume
            
            exercise_name = workout.exercise_name.lower()
            if exercise_name in top_exercise_names:
                weekly_data[week_key][exercise_name].append(workout.weight)
        
        for week in weekly_data:
            for exercise in top_exercise_names:
                weights = weekly_data[week][exercise]
                weekly_data[week][exercise] = sum(weights) / len(weights) if weights else 0
        
        response_data = {
            'weekly_data': weekly_data,
            'top_exercises': top_exercise_names
        }
        
        return jsonify(response_data), 200
        
    except Exception as e:
        current_app.logger.error(f"Error fetching workout history: {e}")
        return jsonify({"error": "Failed to retrieve workout history"}), 500

@main_bp.route("/tools")
@login_required
def workout_tools():
    return render_template("workout_tools.html", title="Tools")

@main_bp.route("/api/workout_plan", methods=['GET'])
def get_workout_plan():
    try:
        plan_entries = models.WorkoutPlan.query.filter_by(user_id=current_user.id).all()
        plan_data = {}
        for entry in plan_entries:
            day = entry.day_of_week
            if day not in plan_data:
                plan_data[day] = []
            plan_data[day].append(entry.to_dict())

        if not plan_data:
             return jsonify({}), 200
        
        return jsonify(plan_data), 200
    except Exception as e:
        current_app.logger.error(f"Error fetching workout plan: {e}")
        return jsonify({"error": "Failed to retrieve workout plan"}), 500

@main_bp.route("/api/get_saved_workout", methods=['GET'])
def get_submitted_this_week():
    try:
        week_offset = int(request.args.get('week_offset', 0))
        today = datetime.now(timezone.utc)
        start_of_week = today - timedelta(days=today.weekday(), weeks=week_offset)
        start_of_week = start_of_week.replace(hour=0, minute=0, second=0, microsecond=0)
        end_of_week = start_of_week + timedelta(days=7)
        
        saved_workout = models.SavedWorkouts.query.filter(
            models.SavedWorkouts.user_id == current_user.id,
            models.SavedWorkouts.save_date >= start_of_week,
            models.SavedWorkouts.save_date < end_of_week
        ).all()
        
        plan_data = {}
        for entry in saved_workout:
            day = entry.day_of_week
            if day not in plan_data:
                plan_data[day] = []
            plan_data[day].append({
                'name': entry.exercise_name,
                'calories': entry.calories_per_set,
                'sets': entry.sets,
                'reps': entry.reps,
                'weight': entry.weight
            })

        return jsonify(plan_data), 200
        
    except Exception as e:
        current_app.logger.error(f"Error fetching workout plan: {e}")
        return jsonify({"error": "Failed to retrieve workout plan"}), 500

@main_bp.route("/api/workout_plan", methods=['POST'])
@login_required
def save_workout_plan():
    try:
        plan_data = request.get_json()
        if plan_data is None:
            return jsonify({"error": "Invalid or empty request body"}), 400

        models.WorkoutPlan.query.filter_by(user_id=current_user.id).delete()
        
        new_entries = []
        if isinstance(plan_data, dict):
            for day, exercises in plan_data.items():
                if isinstance(exercises, list):
                    for exercise in exercises:
                        name = exercise.get('name')
                        calories_per_set = exercise.get('calories') 
                        sets = exercise.get('sets')
                        reps = exercise.get('reps')
                        weight = exercise.get('weight')

                        if not all([name, calories_per_set is not None, sets is not None, reps is not None, weight is not None]):
                             current_app.logger.warning(f"Skipping invalid exercise data for day {day}: {exercise}")
                             continue
                        
                        try:
                            calories_per_set = int(calories_per_set)
                            sets = int(sets)
                            reps = int(reps)
                            weight = int(weight)
                        except (ValueError, TypeError) as ve:
                             current_app.logger.warning(f"Skipping exercise due to invalid numeric value for day {day}: {exercise} - Error: {ve}")
                             continue

                        new_entry = models.WorkoutPlan(
                            user_id=current_user.id,
                            day_of_week=day.lower(),
                            exercise_name=name,
                            calories_per_set=calories_per_set,
                            sets=sets,
                            reps=reps,
                            weight = weight
                        )
                        new_entries.append(new_entry)
                else:
                    current_app.logger.warning(f"Invalid data format for day {day}: Expected a list, got {type(exercises)}")
        else:
             current_app.logger.warning(f"Received plan_data is not a dictionary: {type(plan_data)}")

        if not new_entries:
             current_app.logger.info("No valid exercises found in the submitted plan data. Clearing plan.")
             db.session.commit()
             return jsonify({"message": "Workout plan cleared or no valid exercises submitted."}), 200

        db.session.add_all(new_entries)
        db.session.commit()
        
        return jsonify({"message": "Workout plan saved successfully"}), 201
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Error saving workout plan: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": "Failed to save workout plan", "details": str(e)}), 500

@main_bp.route("/api/save_workout", methods=['POST'])
@login_required
def save_workout():
    try:
        current_plan = models.WorkoutPlan.query.filter_by(user_id=current_user.id).all()
        
        if not current_plan:
            return jsonify({"error": "No workout plan found to save"}), 400

        data = request.get_json()
        week_offset = int(data.get('week_offset', 0))
        now = datetime.now(timezone.utc)
        start_of_week = now - timedelta(days=now.weekday(), weeks=week_offset)
        start_of_week = start_of_week.replace(hour=0, minute=0, second=0, microsecond=0)

        models.SavedWorkouts.query.filter(
            models.SavedWorkouts.user_id == current_user.id,
            models.SavedWorkouts.save_date >= start_of_week,
            models.SavedWorkouts.save_date < start_of_week + timedelta(weeks=1)
        ).delete()
        db.session.commit()

        new_saved_workouts = []
        for workout in current_plan:
            saved_workout = models.SavedWorkouts(
                user_id=current_user.id,
                day_of_week=workout.day_of_week,
                exercise_name=workout.exercise_name,
                calories_per_set=workout.calories_per_set,
                sets=workout.sets,
                reps=workout.reps,
                weight=workout.weight,
                save_date=start_of_week
            )
            new_saved_workouts.append(saved_workout)

        db.session.add_all(new_saved_workouts)
        db.session.commit()

        return jsonify({
            "message": "Workout saved successfully",
            "saved_count": len(new_saved_workouts)
        }), 201

    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Error saving workout: {e}")
        return jsonify({"error": "Failed to save workout", "details": str(e)}), 500

@main_bp.route("/api/shared_workout_history/<int:user_id>", methods=['GET'])
@login_required
def get_shared_workout_history(user_id):
    try:
        shared_plan = models.SharedPlan.query.filter_by(
            sharer_id=user_id,
            recipient_id=current_user.id
        ).first()
        
        if not shared_plan:
            return jsonify({"error": "You don't have permission to view this user's workout history"}), 403

        five_weeks_ago = datetime.now(timezone.utc) - timedelta(weeks=5)
        
        saved_workouts = models.SavedWorkouts.query.filter(
            models.SavedWorkouts.user_id == user_id,
            models.SavedWorkouts.save_date >= five_weeks_ago
        ).order_by(models.SavedWorkouts.save_date).all()
        
        exercise_counts = {}
        for workout in saved_workouts:
            exercise_name = workout.exercise_name.lower()
            exercise_counts[exercise_name] = exercise_counts.get(exercise_name, 0) + 1
        
        top_exercises = sorted(exercise_counts.items(), key=lambda x: x[1], reverse=True)[:3]
        top_exercise_names = [exercise[0] for exercise in top_exercises]
        
        weekly_data = {}
        for workout in saved_workouts:
            workout_date = workout.save_date
            week_start = workout_date - timedelta(days=workout_date.weekday())
            week_key = week_start.strftime('%b %d')
            
            if week_key not in weekly_data:
                weekly_data[week_key] = {
                    'total_volume': 0
                }
                for exercise in top_exercise_names:
                    weekly_data[week_key][exercise] = []
            
            volume = workout.sets * workout.reps * workout.weight
            weekly_data[week_key]['total_volume'] += volume
            
            exercise_name = workout.exercise_name.lower()
            if exercise_name in top_exercise_names:
                weekly_data[week_key][exercise_name].append(workout.weight)
        
        for week in weekly_data:
            for exercise in top_exercise_names:
                weights = weekly_data[week][exercise]
                weekly_data[week][exercise] = sum(weights) / len(weights) if weights else 0
        
        response_data = {
            'weekly_data': weekly_data,
            'top_exercises': top_exercise_names
        }
        
        return jsonify(response_data), 200
        
    except Exception as e:
        current_app.logger.error(f"Error fetching shared workout history: {e}")
        return jsonify({"error": "Failed to retrieve shared workout history"}), 500

@main_bp.route("/api/share_plan", methods=['POST'])
@login_required 
def share_plan():
    if not request.is_json:
        current_app.logger.error(f"Request to /api/share_plan was not JSON. Mimetype: {request.mimetype}. Raw data: {request.data}")
        return jsonify({"error": "Request must be JSON"}), 400

    current_app.logger.info(f"Request is_json check passed. Mimetype: {request.mimetype}")
    data = request.get_json()
    current_app.logger.info(f"Received data for /api/share_plan: {data}")

    recipient_email = data.get('recipientEmail')

    if not recipient_email:
        current_app.logger.error(f"Missing recipientEmail in /api/share_plan request. Received data: {data}")
        return jsonify({"error": "Missing recipientEmail in request body"}), 400

    recipient_user = models.User.query.filter_by(email=recipient_email).first()

    if not recipient_user:
        current_app.logger.warning(f"Recipient user not found: {recipient_email}")
        return jsonify({"error": f"User with email '{recipient_email}' not found."}), 404

    if recipient_user.id == current_user.id:
        current_app.logger.warning(f"User {current_user.id} tried to share plan with themselves.")
        return jsonify({"error": "You cannot share a plan with yourself."}), 400
        
    try:
        new_share = models.SharedPlan(
            sharer_id=current_user.id, 
            recipient_id=recipient_user.id
        )
        db.session.add(new_share)
        db.session.commit()
        
        current_app.logger.info(f"New share record created: ID={new_share.id}, Sharer={current_user.id}, Recipient={recipient_user.id}")
        
        return jsonify({
            "message": f"Plan shared successfully with {recipient_user.email}.",
            "share_details": new_share.to_dict() 
        }), 201

    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Error creating share record from {current_user.id} to {recipient_email} (ID: {recipient_user.id if recipient_user else 'N/A'}): {e}")
        return jsonify({"error": "Failed to create share record in database.", "details": str(e)}), 500

@main_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for("main.login"))

@main_bp.route('/chat', methods=['POST'])
@login_required
def chat():
    user_message = request.json.get('message', '')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    if not openai.api_key:
        current_app.logger.error("OpenAI API key is not set.")
        return jsonify({'error': 'AI service not configured.'}), 500

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful fitness assistant for FitPal. Be concise and encouraging."},
                {"role": "user", "content": user_message}
            ]
        )
        ai_reply = response['choices'][0]['message']['content']
        return jsonify({'reply': ai_reply})
    except Exception as e:
        current_app.logger.error(f"OpenAI API call failed: {e}")
        return jsonify({'error': str(e)}), 500

@main_bp.route('/api/weekly_calories')
@login_required
def weekly_calories():
    try:
        today = datetime.now(timezone.utc).date()
        seven_days_ago = today - timedelta(days=6)
        daily_calories_query = db.session.query(
            func.date(models.SavedWorkouts.save_date).label('date'),
            func.sum(models.SavedWorkouts.calories_per_set * models.SavedWorkouts.sets).label('total_calories')
        ).filter(
            models.SavedWorkouts.user_id == current_user.id,
            func.date(models.SavedWorkouts.save_date) >= seven_days_ago,
            func.date(models.SavedWorkouts.save_date) <= today
        ).group_by(
            func.date(models.SavedWorkouts.save_date)
        ).order_by(
            func.date(models.SavedWorkouts.save_date)
        ).all()

        calories_data = { (seven_days_ago + timedelta(days=i)).strftime('%Y-%m-%d'): 0 for i in range(7) }
        for record in daily_calories_query:
            calories_data[record.date.strftime('%Y-%m-%d')] = record.total_calories if record.total_calories is not None else 0

        if all(v == 0 for v in calories_data.values()):
            week_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
            plan_entries = models.WorkoutPlan.query.filter_by(user_id=current_user.id).all()
            plan_by_day = {day: [] for day in week_days}
            for entry in plan_entries:
                plan_by_day[entry.day_of_week.lower()].append(entry)
            sorted_dates = sorted(calories_data.keys())
            for idx, date_str in enumerate(sorted_dates):
                weekday = week_days[(seven_days_ago + timedelta(days=idx)).weekday()]
                calories_data[date_str] = sum(e.calories_per_set * e.sets for e in plan_by_day[weekday])

        sorted_dates = sorted(calories_data.keys())
        labels = [datetime.strptime(date_str, '%Y-%m-%d').strftime('%a') for date_str in sorted_dates]
        calories_values = [calories_data[date_str] for date_str in sorted_dates]

        return jsonify({'labels': labels, 'calories': calories_values})
    except Exception as e:
        current_app.logger.error(f"Error fetching weekly calories: {e}")
        return jsonify({'error': 'Failed to retrieve weekly calorie data', 'details': str(e)}), 500 