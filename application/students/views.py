from application import app, db
from flask import redirect, render_template, request, url_for
from application.students.models import Student

@app.route("/students", methods=["GET"])
def students_index():
    return render_template("tasks/list.html", students = Student.query.all())

@app.route("/students/new/")
def students_form():
    return render_template("tasks/new.html")

@app.route("/students/<student_id>/", methods=["POST"])
def students_set_done(student_id):
    t = Student.query.get(student_id)
    t.studentnumber = 0
    db.session().commit()

    return redirect(url_for("students_index"))

@app.route("/students/", methods=["POST"])
def students_create():
    t = Student(request.form.get("name"), request.form.get("studentnumber"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("students_index"))
