from flask import Flask, render_template, url_for, redirect, request, jsonify # Import request and jsonify
from config import Config # Import configuration
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy
from flask_migrate import Migrate # Import Migrate

# Initialize Flask application with custom template and static folder paths
app = Flask(__name__, 
            template_folder="templates", 
            static_folder="static",
            instance_relative_config=True,
            instance_path=Config.INSTANCE_FOLDER_PATH)

# Load configuration from Config object
app.config.from_object(Config)

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
@app.route("/login")
def login():
    return render_template("login.html", title="Login")

# Define route for the signup page
@app.route("/signup")
def signup():
    return render_template("signup.html", title="Sign Up")

# Define route for the posts page
@app.route("/posts")
def posts():
    return render_template("posts.html", title="Posts")

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
    """Fetches the current workout plan"""
    try:
        # Query all workout plan entries
        plan_entries = models.WorkoutPlan.query.all()
        # Group entries by day of the week
        plan_by_day = {}
        for entry in plan_entries:
            day = entry.day_of_week
            if day not in plan_by_day:
                plan_by_day[day] = []
            plan_by_day[day].append({
                "name": entry.exercise_name,
                "calories": entry.calories,
                "sets": entry.sets, # Include sets
                "reps": entry.reps  # Include reps
                # Add other fields like sets/reps here if added later
            })
        return jsonify(plan_by_day), 200
    except Exception as e:
        # Add proper logging here
        print(f"Error getting workout plan: {e}")
        return jsonify({"error": "Could not retrieve workout plan"}), 500


@app.route("/api/workout_plan", methods=['POST'])
def save_workout_plan():
    """Saves or updates the workout plan"""
    try:
        # Get JSON data sent from the frontend
        new_plan_data = request.get_json()
        if not new_plan_data:
            return jsonify({"error": "No data provided"}), 400

        # For simplicity, delete all old entries first
        # Warning: Without user authentication, this deletes everyone's plan!
        models.WorkoutPlan.query.delete()

        # Create new plan entries based on the received data
        for day, exercises in new_plan_data.items():
            for exercise in exercises:
                # Ensure necessary data is provided
                if 'name' in exercise and 'calories' in exercise:
                    plan_entry = models.WorkoutPlan(
                        day_of_week=day,
                        exercise_name=exercise['name'],
                        calories=exercise['calories'],
                        # Get sets and reps, default to None if not provided
                        sets=exercise.get('sets'),
                        reps=exercise.get('reps')
                    )
                    db.session.add(plan_entry)
                else:
                    # Optionally skip invalid entries or return an error
                    print(f"Skipping invalid exercise entry: {exercise}")


        # Commit changes to the database
        db.session.commit()
        return jsonify({"message": "Workout plan saved successfully"}), 201 # 201 Created or 200 OK

    except Exception as e:
        db.session.rollback() # Rollback transaction on error
        # Add proper logging here
        print(f"Error saving workout plan: {e}")
        return jsonify({"error": "Could not save workout plan"}), 500

# Run the application in debug mode if this file is executed directly
if __name__ == "__main__":
    app.run(debug=True)