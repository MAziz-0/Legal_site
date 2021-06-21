import os
from flask import Flask, render_template


app = Flask(__name__)

# Created routing to link Python to html files.
@app.route("/")
def index():
    return render_template("index.html", page_name = "Home")


@app.route("/about")
def about():
    return render_template("about.html", page_name = "About Us")


@app.route("/services")
def services():
    return render_template("services.html", page_name = "Services")


@app.route("/contact")
def contact():
    return render_template("contact.html", page_name = "Contact Us")


@app.route("/propertylaw")
def propertylaw():
    return render_template("property.html", page_name = "Property")


@app.route("/litigation")
def litigation():
    return render_template("litigation.html", page_name = "Civil Litigation")


@app.route("/immigration")
def immigration():
    return render_template("immigration.html", page_name = "Home")


@app.route("/family")
def family():
    return render_template("family.html", page_name = "Family")


@app.route("/wills")
def wills():
    return render_template("wills.html", page_name = "Wills & Probate")


@app.route("/employment")
def employment():
    return render_template("employment.html", page_name = "Employment")


@app.route("/mortgage")
def mortgage():
    return render_template("mortgage-info.html", page_name = "How to get a Mortgage in 2021")


@app.route("/employee")
def employee():
    return render_template("employee-info.html", page_name = "Employee Rights")


@app.route("/tax")
def tax():
    return render_template("tax-info.html", page_name = "Capital Gains Tax")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True,
    )
