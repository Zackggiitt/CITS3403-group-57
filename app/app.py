from flask import Flask, render_template, url_for, redirect, request, jsonify, current_app # Import request and jsonify
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import SignupForm, LoginForm
from config import Config # Import configuration
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy
from flask_migrate import Migrate # Import Migrate
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

# "FLASK_SECRET_KEY" is just a placeholder for now, ensure that it is set later
app.secret_key = os.environ.get("FLASK_SECRET_KEY")

csrf = CSRFProtect(app)

# Temporary in-memory "database" to store user details (if we want to test)
# TODO: Replace this with calls to actual database when it is set up
users = {}

# Load configuration from Config object
# Use environment variable or default to 'config.Config'
app.config.from_object(os.environ.get('APP_SETTINGS', 'config.Config'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration tool
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import database models (must be after db initialization)
from app import models

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
        
        # Temporary: retrieve the user from the in-memory store
        # TODO: Replace this with a database query to fetch the user by email
        user = users.get(email)
        
        # Verify hashed password. In production, password is stored securely in your database
        if user and check_password_hash(user["password"], password):
            # User is authenticated
            # TODO: Integrate Flask-Login here for real sessions, for now just print "Logging in"
            print("Logging in:", email)
            return redirect(url_for("profile"))
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
        
        # Temporary: check if the user exists in the in-memory store
        # TODO: Replace this with a database query to check for an existing user by email
        if email in users:
            error = "User already exists with that email."
            return render_template("signup.html", form=form, title="Sign Up", error=error)
        
        # Hash the password before storing it for security
        hashed_password = generate_password_hash(form.password.data)
        
        # Temporary: store the new user in the in-memory "database"
        # TODO: Replace this with a database INSERT operation
        users[email] = {
            "first_name": form.first_name.data,
            "last_name": form.last_name.data,
            "email": email,
            "password": hashed_password,
        }
        print("New user registered:", email)
        return redirect(url_for("login"))
    
    return render_template("signup.html", form=form, title="Sign Up", error=error)

# Define route for the posts page
@app.route("/posts")
def posts():
    mock_user_id = 1 
    
    my_plans_query = models.WorkoutPlan.query.filter_by(user_id=mock_user_id)
    my_plan_entries = my_plans_query.all()
    my_plans_by_day = {day: [] for day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]}
    for entry in my_plan_entries:
        if entry.day_of_week in my_plans_by_day:
            my_plans_by_day[entry.day_of_week].append(entry.to_dict())
    
    ordered_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    ordered_my_plans_by_day = {day: my_plans_by_day.get(day, []) for day in ordered_days}

    mock_recipient_identifier = "user2" # IMPORTANT: Change "user2" to an actual recipient_identifier in your SharedPlan table

    # --- New logic for "Plans Shared With Me" ---
    # 1. Subquery to find the latest shared_at for each sharer to the recipient
    latest_shared_times_subq = db.session.query(
        models.SharedPlan.sharer_id,
        func.max(models.SharedPlan.shared_at).label('latest_shared_at')
    ).filter(
        models.SharedPlan.recipient_identifier == mock_recipient_identifier
    ).group_by(
        models.SharedPlan.sharer_id
    ).subquery('latest_shared_times_subq')

    # 2. Query to get the actual SharedPlan records corresponding to these latest times
    latest_share_records_for_recipient = db.session.query(models.SharedPlan).join(
        latest_shared_times_subq,
        (models.SharedPlan.sharer_id == latest_shared_times_subq.c.sharer_id) &
        (models.SharedPlan.shared_at == latest_shared_times_subq.c.latest_shared_at)
    ).filter( # Ensure recipient match is still part of the main query for clarity/safety
        models.SharedPlan.recipient_identifier == mock_recipient_identifier
    ).order_by(models.SharedPlan.sharer_id).all() # Order by sharer_id for consistent dropdown later

    sharers_for_dropdown = []
    latest_plans_data_for_js = {}

    for share_record in latest_share_records_for_recipient:
        sharer_id = share_record.sharer_id
        
        # Add sharer to dropdown list if not already (though subquery should ensure uniqueness by sharer_id)
        # For display purposes, we can format a name.
        sharers_for_dropdown.append({
            'id': sharer_id,
            'display_text': f"Plan from User {sharer_id}" 
        })

        sharer_workout_entries = models.WorkoutPlan.query.filter_by(user_id=sharer_id).all()
        
        sharer_plans_by_day = {day: [] for day in ordered_days} # Use ordered_days for consistency
        has_plan_entries = False
        for entry in sharer_workout_entries:
            # Ensure day_of_week is one of the predefined keys
            day_key = entry.day_of_week.lower()
            if day_key in sharer_plans_by_day:
                sharer_plans_by_day[day_key].append(entry.to_dict())
                has_plan_entries = True
        
        # Ensure all days are present in the final dict, even if empty
        ordered_sharer_plans = {day: sharer_plans_by_day.get(day, []) for day in ordered_days}

        latest_plans_data_for_js[str(sharer_id)] = { # Use string key for JS object
            'sharer_id': sharer_id, # Keep original int id if needed elsewhere
            'shared_at': share_record.shared_at.strftime('%Y-%m-%d %H:%M:%S'),
            'recipient_identifier': share_record.recipient_identifier,
            'plan_details': ordered_sharer_plans,
            'plan_exists': has_plan_entries
        }
        
    return render_template(
        "posts.html", 
        title="My Workout Week & Shared Plans", 
        my_plans_data=ordered_my_plans_by_day, 
        mock_user_id=mock_user_id, 
        # Pass new data structures to the template
        sharers_for_dropdown=sharers_for_dropdown,
        latest_plans_data_json=json.dumps(latest_plans_data_for_js), # Serialize to JSON string
        mock_recipient_identifier=mock_recipient_identifier
    )

# Define route for the user profile page
@app.route("/profile")
def profile():
    return render_template("profile.html", title="Profile")

# Define route for the workout tools page
@app.route("/tools")
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

                        # Basic validation
                        if not all([name, calories_per_set is not None, sets is not None, reps is not None]):
                             current_app.logger.warning(f"Skipping invalid exercise data for day {day}: {exercise}")
                             continue # Skip this exercise if data is missing
                        
                        try:
                            # Ensure numeric types
                            calories_per_set = int(calories_per_set)
                            sets = int(sets)
                            reps = int(reps)
                        except (ValueError, TypeError) as ve:
                             current_app.logger.warning(f"Skipping exercise due to invalid numeric value for day {day}: {exercise} - Error: {ve}")
                             continue # Skip if conversion fails

                        # Create new entry using correct model field names
                        new_entry = models.WorkoutPlan(
                            day_of_week=day.lower(),
                            exercise_name=name,
                            calories=calories_per_set, # Map to the 'calories' field in model
                            sets=sets,
                            reps=reps
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
    
@app.route("/api/mock_share_plan", methods=['POST'])
def mock_share_plan():
    """
    Mock endpoint to simulate sharing a workout plan.
    Accepts a target user identifier and the ID of the user sharing the plan.
    Now saves the record to SharedPlan table.
    """
    if not request.is_json:
        current_app.logger.error("Request to /api/mock_share_plan was not JSON")
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    current_app.logger.info(f"Received data for /api/mock_share_plan: {data}")

    target_user = data.get('targetUser')
    sharer_user_id = data.get('sharerUserId')

    if not target_user or sharer_user_id is None: 
        current_app.logger.error(
            f"Missing data for /api/mock_share_plan - "
            f"target_user: {target_user}, sharer_user_id: {sharer_user_id}"
        )
        return jsonify({"error": "Missing targetUser or sharerUserId in request body"}), 400

    try:
        new_share = models.SharedPlan(
            sharer_id=sharer_user_id,
            recipient_identifier=target_user
            # shared_at will be set by default by the model
        )
        db.session.add(new_share)
        db.session.commit()
        
        current_app.logger.info(f"New share record created: ID={new_share.id}, Sharer={sharer_user_id}, Recipient={target_user}")
        
        return jsonify({
            "message": "Plan shared and record created successfully.",
            "share_details": new_share.to_dict() # Optionally return details of the created share
        }), 201 # 201 Created is more appropriate here

    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Error creating share record: {e}")
        return jsonify({"error": "Failed to create share record in database.", "details": str(e)}), 500

# Run the application in debug mode if this file is executed directly
if __name__ == "__main__":
    app.run(debug=True)