from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.students.models import Student
from application.students.forms import StudentForm

@app.route("/students", methods=["GET"])
def students_index():
    return render_template("students/list.html", students = Student.query.all())

@app.route("/students/new/")
@login_required
def students_form():
    return render_template("students/new.html", form = StudentForm())

@app.route("/students/<student_id>/", methods=["POST"])
@login_required
def students_set_done(student_id):
    t = Student.query.get(student_id)
    t.studentnumber = 0
    db.session().commit()

    return redirect(url_for("students_index"))

@app.route("/students/", methods=["POST"])
@login_required
def students_create():
    form = StudentForm(request.form)

    if not form.validate():
        return render_template("students/new.html", form = form)

    t = Student(form.name.data)
    t.studentnumber = form.number.data
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("students_index"))
