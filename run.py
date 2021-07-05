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


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if username already exists in db
        registered_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )
        flash(
            "Thanks {}, we have received your message!".format(request.form.get("name"))
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
    return render_template("register.html", page_title="Register")


@app.route("/propertylaw")
def propertylaw():
    return render_template("property.html", page_name="Property")


@app.route("/litigation")
def litigation():
    return render_template("litigation.html", page_name="Civil Litigation")


@app.route("/immigration")
def immigration():
    return render_template("immigration.html", page_name="Home")


@app.route("/family")
def family():
    return render_template("family.html", page_name="Family")


@app.route("/wills")
def wills():
    return render_template("wills.html", page_name="Wills & Probate")


@app.route("/employment")
def employment():
    return render_template("employment.html", page_name="Employment")


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


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True,
    )