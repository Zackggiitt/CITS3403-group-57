from flask import Flask, render_template, url_for, redirect, request, jsonify, current_app, flash # Import flash
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import SignupForm, LoginForm
from config import Config # Import configuration
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy
from flask_migrate import Migrate # Import Migrate
# --- Flask-Login Imports ---
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user 

import os
from dotenv import load_dotenv
from sqlalchemy import desc # Added for ordering
from sqlalchemy.sql import func
import json

# Load environment variables from .env file
load_dotenv()

# Initialize Flask application with custom template and static folder paths
app = Flask(__name__, 
            template_folder="templates", 
            static_folder="static",
            instance_relative_config=True,
            instance_path=Config.INSTANCE_FOLDER_PATH)

# TODO: "FLASK_SECRET_KEY" is just a placeholder for now, ensure that it is set later
app.secret_key = os.environ.get("FLASK_SECRET_KEY")

csrf = CSRFProtect(app)

# Load configuration from Config object
# Use environment variable or default to 'config.Config'
app.config.from_object(os.environ.get('APP_SETTINGS', 'config.Config'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration tool
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# --- Flask-Login Setup ---
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login' # Specifies the route Flask-Login redirects to when login is required
login_manager.login_message = "Please log in to access this page." # Optional: Custom message
login_manager.login_message_category = "info" # Optional: Flash message category

# Import database models (must be after db initialization)
from app import models
from app.models import User # Explicitly import User model for clarity

# --- User Loader Callback ---
# This callback is used to reload the user object from the user ID stored in the session
@login_manager.user_loader
def load_user(user_id):
    # Since user_id is just the primary key of our user table, use it directly
    return User.query.get(int(user_id))

# Define route for the home page
@app.route("/")
def index():
    return render_template("index.html", title='Home')

# Define route for the login page
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    error = None

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        
        # Query the database for the user
        user = User.query.filter_by(email=email).first()
        
        # Verify hashed password
        if user and check_password_hash(user.password_hash, password): # Corrected: user.password -> user.password_hash
            # --- Use Flask-Login's login_user ---
            login_user(user) # Log the user in
            flash('Logged in successfully.') # Optional: Flash message
            # Redirect to the page user tried to access before login, or profile if none
            next_page = request.args.get('next')
            return redirect(next_page or url_for("profile"))
        else:
            error = "Invalid email or password."
    
    return render_template("login.html", form=form, title="Login", error=error)

# Define route for the signup page
@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    error = None

    if form.validate_on_submit():
        email = form.email.data
        
        # Check if the user already exists in the database
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            error = "User already exists with that email."
            return render_template("signup.html", form=form, title="Sign Up", error=error)
        
        # Hash the password before storing it for security
        hashed_password = generate_password_hash(form.password.data)
        
        # Create a new user and add to the database
        new_user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=email,
            # Corrected: Use the correct column name 'password_hash' from your schema
            password_hash=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        flash("Account created successfully! Please log in.")
        return redirect(url_for("login"))
    
    return render_template("signup.html", form=form, title="Sign Up", error=error)

# Define route for the posts page
@app.route("/posts")
@login_required # Add decorator to require login for this page
def posts():
    # --- Get current user's workout plan ---
    # Remove mock_user_id
    my_plans_query = models.WorkoutPlan.query.filter_by(user_id=current_user.id) # Use current_user.id
    my_plan_entries = my_plans_query.all()
    my_plans_by_day = {day: [] for day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]}
    for entry in my_plan_entries:
        if entry.day_of_week in my_plans_by_day:
            my_plans_by_day[entry.day_of_week].append(entry.to_dict())
    
    ordered_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    ordered_my_plans_by_day = {day: my_plans_by_day.get(day, []) for day in ordered_days}

    # --- Get plans shared with the current user ---
    # Remove mock_recipient_identifier

    # 1. Subquery to find the latest shared_at for each sharer to the current user
    latest_shared_times_subq = db.session.query(
        models.SharedPlan.sharer_id,
        func.max(models.SharedPlan.shared_at).label('latest_shared_at')
    ).filter(
        models.SharedPlan.recipient_id == current_user.id # Use recipient_id and current_user.id
    ).group_by(
        models.SharedPlan.sharer_id
    ).subquery('latest_shared_times_subq')

    # 2. Query to get the actual SharedPlan records corresponding to these latest times
    latest_share_records_for_recipient = db.session.query(models.SharedPlan).join(
        latest_shared_times_subq,
        (models.SharedPlan.sharer_id == latest_shared_times_subq.c.sharer_id) &
        (models.SharedPlan.shared_at == latest_shared_times_subq.c.latest_shared_at)
    ).filter( 
        models.SharedPlan.recipient_id == current_user.id # Filter again for safety/clarity
    ).order_by(models.SharedPlan.sharer_id).all() 

    sharers_for_dropdown = []
    latest_plans_data_for_js = {}

    for share_record in latest_share_records_for_recipient:
        # Access the sharer User object via the relationship
        sharer_user = share_record.sharer 
        if not sharer_user: # Check if sharer exists (should always exist due to FK)
            continue 
        
        sharer_id = sharer_user.id
        sharer_display_name = f"{sharer_user.first_name} {sharer_user.last_name}" # Get sharer's name

        sharers_for_dropdown.append({
            'id': sharer_id,
            'display_text': f"Plan from {sharer_display_name}" # Use sharer's name
        })

        # Fetch workout entries for this specific sharer
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
            'sharer_name': sharer_display_name, # Add sharer name to JS data
            'shared_at': share_record.shared_at.strftime('%Y-%m-%d %H:%M:%S'),
            'recipient_id': share_record.recipient_id, # Now using recipient_id
            'plan_details': ordered_sharer_plans,
            'plan_exists': has_plan_entries
        }
        
    return render_template(
        "posts.html", 
        title="My Workout Week & Shared Plans", 
        my_plans_data=ordered_my_plans_by_day, 
        # Remove mock_user_id and mock_recipient_identifier from template context
        sharers_for_dropdown=sharers_for_dropdown,
        latest_plans_data_json=json.dumps(latest_plans_data_for_js) # Serialize to JSON string
    )

# Define route for the user profile page
@app.route("/profile")
@login_required # Add decorator to require login for this page
def profile():
    # You can now access the logged-in user via current_user
    # Example: return render_template("profile.html", title="Profile", user=current_user)
    return render_template("profile.html", title="Profile")

# Define route for the workout tools page
@app.route("/tools")
@login_required # Add decorator to require login for this page
def workout_tools():
    return render_template("workout_tools.html", title="Tools")

@app.route("/api/workout_plan", methods=['GET'])
def get_workout_plan():
    """Fetches the entire workout plan from the database."""
    try:
        # Query all workout plan entries
        plan_entries = models.WorkoutPlan.query.all()
        
        # Organize data by day
        plan_data = {}
        for entry in plan_entries:
            day = entry.day_of_week # Use the correct attribute name
            if day not in plan_data:
                plan_data[day] = []
            # Use the to_dict method which now includes sets and reps
            plan_data[day].append(entry.to_dict())

        # Return the organized data
        # Check if plan_data is empty and return appropriate response
        if not plan_data:
             # Return an empty object or a 404 Not Found status
             # Returning empty object is often preferred for GET requests expecting a collection
             return jsonify({}), 200 # Or return jsonify({"message": "No workout plan found"}), 404
        
        return jsonify(plan_data), 200
    except Exception as e:
        current_app.logger.error(f"Error fetching workout plan: {e}")
        return jsonify({"error": "Failed to retrieve workout plan"}), 500

@app.route("/api/workout_plan", methods=['POST'])
@login_required # Secure this API endpoint
def save_workout_plan():
    """Saves the workout plan received from the frontend."""
    try:
        plan_data = request.get_json()
        # Modified check: Allow empty dictionary {} but reject None or other falsy values
        if plan_data is None:
            return jsonify({"error": "Invalid or empty request body"}), 400

        # Clear existing plan entries (assuming a single plan for now)
        models.WorkoutPlan.query.delete()
        
        new_entries = []
        # Check if plan_data is actually a dictionary before iterating
        if isinstance(plan_data, dict):
            for day, exercises in plan_data.items():
                if isinstance(exercises, list):
                    for exercise in exercises:
                        # Ensure required fields are present and extract them
                        name = exercise.get('name')
                        # Frontend sends 'calories' which is calories_per_set
                        calories_per_set = exercise.get('calories') 
                        sets = exercise.get('sets')
                        reps = exercise.get('reps')
                        weight = exercise.get('weight')

                        # Basic validation
                        if not all([name, calories_per_set is not None, sets is not None, reps is not None, weight is not None]):
                             current_app.logger.warning(f"Skipping invalid exercise data for day {day}: {exercise}")
                             continue # Skip this exercise if data is missing
                        
                        try:
                            # Ensure numeric types
                            calories_per_set = int(calories_per_set)
                            sets = int(sets)
                            reps = int(reps)
                            weight = int(weight)
                        except (ValueError, TypeError) as ve:
                             current_app.logger.warning(f"Skipping exercise due to invalid numeric value for day {day}: {exercise} - Error: {ve}")
                             continue # Skip if conversion fails

                        # Create new entry using validated data
                        new_entry = models.WorkoutPlan(
                            user_id=current_user.id, # Use current_user.id instead of hardcoded/mock ID
                            day_of_week=day.lower(), # Normalize day name
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
             # Handle case where plan_data is not a dictionary (e.g., if {} was sent but we want to be extra safe)
             current_app.logger.warning(f"Received plan_data is not a dictionary: {type(plan_data)}")


        if not new_entries:
             current_app.logger.info("No valid exercises found in the submitted plan data. Clearing plan.")
             # Commit the delete if no new entries are added
             db.session.commit()
             return jsonify({"message": "Workout plan cleared or no valid exercises submitted."}), 200


        # Add all new entries to the session and commit
        db.session.add_all(new_entries)
        db.session.commit()
        
        return jsonify({"message": "Workout plan saved successfully"}), 201 # 201 Created
    except Exception as e:
        db.session.rollback() # Rollback in case of error
        current_app.logger.error(f"Error saving workout plan: {e}")
        import traceback
        traceback.print_exc() # Print detailed traceback to server logs
        return jsonify({"error": "Failed to save workout plan", "details": str(e)}), 500
    
@app.route("/api/share_plan", methods=['POST'])
@login_required 
def share_plan(): # Renamed function
    """
    Endpoint to handle sharing the current user's workout plan with another user.
    Accepts the recipient user's email address.
    Saves the share record to SharedPlan table.
    """
    if not request.is_json:
        current_app.logger.error("Request to /api/share_plan was not JSON")
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    current_app.logger.info(f"Received data for /api/share_plan: {data}")

    recipient_email = data.get('recipientEmail') # Expect recipient email

    if not recipient_email:
        current_app.logger.error("Missing recipientEmail in /api/share_plan request")
        return jsonify({"error": "Missing recipientEmail in request body"}), 400

    # Find the recipient user by email
    recipient_user = User.query.filter_by(email=recipient_email).first()

    if not recipient_user:
        current_app.logger.warning(f"Recipient user not found: {recipient_email}")
        return jsonify({"error": f"User with email '{recipient_email}' not found."}), 404 # Not Found

    # Prevent users from sharing with themselves
    if recipient_user.id == current_user.id:
        current_app.logger.warning(f"User {current_user.id} tried to share plan with themselves.")
        return jsonify({"error": "You cannot share a plan with yourself."}), 400
        
    # Check if this exact share (sharer to recipient) already exists to prevent duplicates
    # Note: We might allow re-sharing to update the timestamp, depending on requirements.
    # For now, let's prevent exact duplicates if needed, or just allow re-sharing.
    # Allowing re-sharing (which updates the timestamp) is simpler for now.

    try:
        # Create the share record using current_user and recipient_user IDs
        new_share = models.SharedPlan(
            sharer_id=current_user.id, 
            recipient_id=recipient_user.id
            # shared_at will be set by default by the model
        )
        db.session.add(new_share)
        db.session.commit()
        
        current_app.logger.info(f"New share record created: ID={new_share.id}, Sharer={current_user.id}, Recipient={recipient_user.id}")
        
        # Include recipient details in the response for clarity
        return jsonify({
            "message": f"Plan shared successfully with {recipient_user.email}.",
            "share_details": new_share.to_dict() 
        }), 201

    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Error creating share record from {current_user.id} to {recipient_email} (ID: {recipient_user.id if recipient_user else 'N/A'}): {e}")
        return jsonify({"error": "Failed to create share record in database.", "details": str(e)}), 500

# --- Logout Route ---
@app.route("/logout")
@login_required # Ensure user is logged in to log out
def logout():
    logout_user() # Log the user out
    flash("You have been logged out.")
    return redirect(url_for('login')) # Redirect to login page after logout

# Run the application in debug mode if this file is executed directly
if __name__ == "__main__":
    app.run(debug=True)