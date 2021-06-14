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
   


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True,
    )
