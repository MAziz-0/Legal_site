import os
import json
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
# Created routing to link Python to html files.


@app.route("/")
def index():
    return render_template("index.html", page_name="Home")


@app.route("/about")
def about():
    data = []
    with open("data/firm.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", firm=data)


@app.route("/services")
def services():
    return render_template("services.html", page_name="Services")


@app.route("/")
@app.route("/get_tasks")
def task():
    tasks = list(mongo.db.tasks.find())
    return render_template("myquestions.html", tasks=tasks)

# Searching existing queries
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    tasks = list(mongo.db.tasks.find({"$text": {"$search": query}}))
    return render_template("myquestions.html", tasks=tasks)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if username already exists in db
        registered_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )
        if registered_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
        }
        mongo.db.users.insert_one(register)
        # Put the new user into a new session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html", page_title="Register")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if username exists in MondoDB
        registered_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if registered_user:
            # Flash message - Hash password check
            if check_password_hash(
                registered_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Collect the session username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # Remove user from session
    flash("You have been logged out")
    session.clear()
    return redirect(url_for("login"))


@app.route("/propertylaw")
def propertylaw():
    return render_template("property.html", page_name="Property Services")


@app.route("/litigation")
def litigation():
    return render_template(
        "litigation.html", page_name="Civil Litigation Services")


@app.route("/immigration")
def immigration():
    return render_template(
        "immigration.html", page_name="Immigration Services")


@app.route("/family")
def family():
    return render_template(
        "family.html", page_name="Family Law")


@app.route("/wills")
def wills():
    return render_template(
        "wills.html", page_name="Wills and Probate")


@app.route("/employment")
def employment():
    return render_template("employment.html", page_name="Employment Law")


@app.route("/mortgage")
def mortgage():
    return render_template(
        "mortgage-info.html", page_name="How to get a Mortgage in 2021"
    )


@app.route("/employee")
def employee():
    return render_template("employee-info.html", page_name="Employee Rights")


@app.route("/tax")
def tax():
    return render_template("tax-info.html", page_name="Capital Gains Tax")


@app.route("/contact")
def contact():
    return render_template("contact.html", page_name="Contact")

# Creating a new query
@app.route("/add_question", methods=["GET", "POST"])
def add_question():
    if request.method == "POST":
        question = {
            "task_num": request.form.get("task_num"),
            "category_name": request.form.get("category_name"),
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "created_by": session["user"]
        }
        mongo.db.tasks.insert_one(question)
        flash("Submitted successfully. You will receive an answer shortly.")
        return redirect(url_for("add_question"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_question.html", categories=categories)

# Editing Query
@app.route("/edit_question/<task_id>", methods=["GET", "POST"])
def edit_question(task_id):
    if request.method == "POST":
        update = {
            "task_num": request.form.get("task_num"),
            "category_name": request.form.get("category_name"),
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description"),
            "created_by": session["user"]
        }
        mongo.db.tasks.update({"_id": ObjectId(task_id)}, update)
        flash("Update successful")
        return redirect(url_for("add_question"))
    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_question.html", task=task, categories=categories)

# Deleting a query
@app.route("/delete_question/<task_id>")
def delete_question(task_id):
    mongo.db.tasks.remove({"_id": ObjectId(task_id)})
    flash("Successfully Deleted")
    return redirect(url_for("task"))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True,
    )
