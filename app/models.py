from app import db # Import the db instance from app.py
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timezone # Import datetime for timestamping
from flask_login import UserMixin # Import UserMixin

class User(UserMixin, db.Model): # Inherit from UserMixin
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    bio = db.Column(db.String(200), nullable=True, default="Edit your profile to add a bio!")
    bmr = db.Column(db.Integer, nullable=True, default=0)
    password_hash = db.Column(db.String(128), nullable=False)
    
    # Relationships
    # One-to-Many: A user can have many workout plan entries
    workout_plans = db.relationship('WorkoutPlan', back_populates='user', lazy='dynamic', cascade="all, delete-orphan")
    # One-to-Many: A user can share many plans (as the sharer)
    shared_plans_sent = db.relationship('SharedPlan', foreign_keys='SharedPlan.sharer_id', back_populates='sharer', lazy='dynamic', cascade="all, delete-orphan")
    # One-to-Many: A user can receive many shared plans (as the recipient)
    shared_plans_received = db.relationship('SharedPlan', foreign_keys='SharedPlan.recipient_id', back_populates='recipient', lazy='dynamic', cascade="all, delete-orphan")
    # One-to-Many: A user can have many saved workout plans
    saved_workouts = db.relationship('SavedWorkouts', back_populates='user', lazy='dynamic', cascade="all, delete-orphan")

    def __repr__(self):
        return f'<User {self.email}>'
    
    def set_password(self, password):
        if not isinstance(password, str) or not password:
            raise TypeError("Password must be a non-empty string")
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
            'email': self.email,
            'bio': self.bio,
            'bmr': self.bmr
        }


class WorkoutPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Store the day of the week, e.g., "monday", "tuesday"
    day_of_week = db.Column(db.String(10), nullable=False, index=True)
    exercise_name = db.Column(db.String(100), nullable=False)
    calories_per_set = db.Column(db.Integer, nullable=False)
    # New fields, allow null values
    sets = db.Column(db.Integer, nullable=False, default=3)
    reps = db.Column(db.Integer, nullable=False, default=10)
    weight = db.Column(db.Integer, nullable=False, default=5)
    # Foreign Key to User table
    # Made non-nullable as a workout plan must belong to a user
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    
    # Relationship back to User
    user = db.relationship('User', back_populates='workout_plans')

    def __repr__(self):
        # String representation for debugging
        return f'<WorkoutPlan {self.day_of_week}: {self.exercise_name} {self.sets}x{self.reps} at {self.weight}kg by User {self.user_id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'day': self.day_of_week,
            'name': self.exercise_name,
            'calories': self.calories_per_set, # Match the potentially renamed column
            'sets': self.sets,
            'reps': self.reps,
            'weight': self.weight
        }

class SharedPlan(db.Model):
    __tablename__ = 'shared_plan'

    id = db.Column(db.Integer, primary_key=True)
    # Foreign Key to the user who shared the plan
    sharer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    # Foreign Key to the user who received the plan (replaces recipient_identifier)
    recipient_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    shared_at = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))

    # Relationships
    # Many-to-One: Link back to the sharer User
    sharer = db.relationship('User', foreign_keys=[sharer_id], back_populates='shared_plans_sent')
    # Many-to-One: Link back to the recipient User
    recipient = db.relationship('User', foreign_keys=[recipient_id], back_populates='shared_plans_received')

    def __repr__(self):
        return f'<SharedPlan id={self.id} from User {self.sharer_id} to User {self.recipient_id} at={self.shared_at}>'

    def to_dict(self):
        return {
            'id': self.id,
            'sharer_id': self.sharer_id,
            'recipient_id': self.recipient_id,
            'shared_at': self.shared_at.isoformat()
        }
    
class SavedWorkouts(db.Model):
    #Most of the columns are the same as the other workout tables
    id = db.Column(db.Integer, primary_key=True)
    day_of_week = db.Column(db.String(10), nullable=False, index=True)
    exercise_name = db.Column(db.String(100), nullable=False)
    calories_per_set = db.Column(db.Integer, nullable=False)
    sets = db.Column(db.Integer, nullable=False, default=3)
    reps = db.Column(db.Integer, nullable=False, default=10)
    weight = db.Column(db.Integer, nullable=False, default=5)

    #The date the workouts were saved
    save_date = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))

    #Add the foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    
    #Add the relationship back to User
    user = db.relationship('User', back_populates='saved_workouts')