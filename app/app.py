import os
from flask import Flask, render_template, url_for, redirect, request
from flask_wtf.csrf import CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash
from forms import SignupForm, LoginForm

app = Flask(__name__, template_folder="templates", static_folder="static")

# "FLASK_SECRET_KEY" is just a placeholder for now, ensure that it is set later
app.secret_key = os.environ.get("FLASK_SECRET_KEY")

csrf = CSRFProtect(app)

# Temporary in-memory "database" to store user details (if we want to test)
# TODO: Replace this with calls to actual database when it is set up
users = {}

@app.route("/")
def index():
    return render_template("index.html", title='Home')

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

@app.route("/posts")
def posts():
    return render_template("posts.html", title="Posts")

@app.route("/profile")
def profile():
    return render_template("profile.html", title="Profile")

@app.route("/tools")
def workout_tools():
    return render_template("workout_tools.html", title="Tools")

if __name__ == "__main__":
    app.run(debug=True)