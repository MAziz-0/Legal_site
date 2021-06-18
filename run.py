import os
from flask import Flask, render_template


app = Flask(__name__)

# Created routing to link Python to html files.
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/propertylaw")
def propertylaw():
    return render_template("property.html")


@app.route("/litigation")
def litigation():
    return render_template("litigation.html")


@app.route("/immigration")
def immigration():
    return render_template("immigration.html")


@app.route("/family")
def family():
    return render_template("family.html")


@app.route("/wills")
def wills():
    return render_template("wills.html")


@app.route("/employment")
def employment():
    return render_template("employment.html")


@app.route("/mortgage")
def mortgage():
    return render_template("mortgage-info.html")


@app.route("/employee")
def employee():
    return render_template("employee-info.html")


@app.route("/tax")
def tax():
    return render_template("tax-info.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True,
    )
