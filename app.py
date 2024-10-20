from cs50 import SQL
from flask import Flask, flash, redirect, render_template, session, request
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///users.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    user_id = session["user_id"]

    #get user info
    user = db.execute("SELECT * FROM users WHERE id = ?", user_id)

    #if the request method is POST
    if request.method == "POST":
        #check if it's a task deletion
        if request.form.get("task_id"):
            task_id = request.form.get("task_id")
            #delete the task
            db.execute("DELETE FROM todos_new WHERE id = ?", task_id)
            return redirect("/")  #redirect to avoid form resubmission

        #add new task
        task = request.form.get("task")
        if task:
            db.execute("INSERT INTO todos_new (user_id, task) VALUES (?, ?)", user_id, task)
            return redirect("/")  #redirect to avoid form resubmission

    #get and display all tasks
    todos = db.execute("SELECT * FROM todos_new WHERE user_id = ?", user_id)

    return render_template("index.html", user=user[0], todos_new=todos)


@app.route("/logout")
def logout():
    session.clear()

    return redirect("/")

@app.route("/login", methods=["POST", "GET"])
def login():

    session.clear()

    if request.method == "POST":
        if not request.form.get("username"):
            flash("username and password required")
            return render_template("login.html")
        elif not request.form.get("password"):
            flash("username and password required")
            return render_template("login.html")

        #selects a row in users db w the given username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        #checks if the username exists and if the password is valid
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hashed"], request.form.get("password")
        ):
            flash("invalid password or username")
            return render_template("login.html")

        #saves the user in the session
        session["user_id"] = rows[0]["id"]

        return redirect("/")

    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        #checks if the username exists
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        if not username or not password:
            flash("username and password required")
            return render_template("registration.html")
        if len(rows) > 0:
            flash("username already exists")
            return render_template("registration.html")

        hashed = generate_password_hash(password)

        try:
            db.execute("INSERT INTO users (username, hashed) VALUES (?, ?)", username, hashed)
        except ValueError:
            flash("the username already exists")
            return render_template("registration.html")

        return redirect("/")


    return render_template("registration.html")
