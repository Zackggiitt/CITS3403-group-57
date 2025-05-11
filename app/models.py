from app.app import db # Import the db instance from app.py
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(128), nullable=False)

    workout_plans = db.relationship('WorkoutPlan', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.email}>'
    
    def set_password(self, password):
        # Hash and set user's password
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        # Verify the user's password
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        # Converts the user instance to a dictionary
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }

class WorkoutPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Store the day of the week, e.g., "monday", "tuesday"
    day_of_week = db.Column(db.String(10), nullable=False, index=True)
    exercise_name = db.Column(db.String(100), nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    # New fields, allow null values
    sets = db.Column(db.Integer, nullable=False, default=3)
    reps = db.Column(db.Integer, nullable=False, default=10)
    # Future fields could be added here
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # Example for user association

    def __repr__(self):
        # String representation for debugging
        return f'<WorkoutPlan {self.day_of_week}: {self.exercise_name} {self.sets}x{self.reps}>'

    def to_dict(self):
        return {
            'id': self.id,
            'day': self.day_of_week,
            'name': self.exercise_name,
            'calories': self.calories,
            'sets': self.sets,
            'reps': self.reps
        }