from flask import Flask, render_template, url_for, redirect

app = Flask(__name__, template_folder="../templates", static_folder="../static")

@app.route("/")
def index():
    return render_template("index.html", title='Home')

@app.route("/login")
def login():
    return render_template("login.html", title="Login")

@app.route("/signup")
def signup():
    return render_template("signup.html", title="Sign Up")

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