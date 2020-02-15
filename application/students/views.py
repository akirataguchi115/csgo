from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.students.models import Student 
from application.students.forms import LoginForm, RegisterForm

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
    u = Student("General User", form.username.data, form.password.data)

    db.session().add(u)
    db.session().commit()
    return redirect(url_for("index"))
