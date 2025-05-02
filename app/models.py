from app.app import db # Import the db instance from app.py

class WorkoutPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Store the day of the week, e.g., "monday", "tuesday"
    day_of_week = db.Column(db.String(10), nullable=False, index=True)
    exercise_name = db.Column(db.String(100), nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    # New fields, allow null values
    sets = db.Column(db.Integer, nullable=True)
    reps = db.Column(db.Integer, nullable=True)
    # Future fields could be added here
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # Example for user association

    def __repr__(self):
        # String representation for debugging
        return f'<WorkoutPlan {self.day_of_week}: {self.exercise_name}>'