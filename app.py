from flask import Flask, render_template, url_for, redirect

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/posts")
def posts():
    return render_template("posts.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/tools")
def workout_tools():
    return render_template("workout_tools.html")

if __name__ == "__main__":
    app.run(debug=True)