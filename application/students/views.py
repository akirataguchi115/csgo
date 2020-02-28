from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db, login_required
from application.students.models import Student 
from application.students.forms import LoginForm, RegisterForm, UpdateForm

@app.route("/students/login", methods = ["GET", "POST"])
def students_login():
    if request.method == "GET":
        return render_template("students/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = Student.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("students/loginform.html", form = form,
                               error = "No such username or password")


    login_user(user)
    return redirect(url_for("index"))

@app.route("/students/logout")
def students_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/students/register", methods = ["GET", "POST"])
def students_register():
    if request.method == "GET":
        return render_template("students/registerform.html", form = RegisterForm())

    form = RegisterForm(request.form)
    student = Student(form.username.data, form.password.data, form.name.data, form.studentnumber.data)

    db.session().add(student)
    db.session().commit()
    return redirect(url_for("index"))

@app.route("/students/update/<student_id>/", methods = ["GET", "POST"])
@login_required(role="USER")
def students_update(student_id):
    if request.method == "GET":
        return render_template("students/updateform.html", form = UpdateForm())

    form = UpdateForm(request.form) 
    student = Student.query.get(student_id)
    if form.passwordagain.data == student.password:
        student.password = form.password.data
        student.name = form.name.data
    
        db.session().commit()
        return redirect(url_for("index"))
    else:
        return redirect(url_for("students_update", student_id=student_id))

@app.route("/students/delete/<student_id>", methods = ["POST"])
@login_required(role="USER")
def students_delete(student_id):
    student_to_delete = Student.query.get(student_id)
    db.session().delete(student_to_delete)
    db.session().commit()
    return redirect(url_for("students_logout"))
