from flask import render_template
from application import app
from application.students.models import Student

@app.route("/")
def index():
    return render_template("index.html")
