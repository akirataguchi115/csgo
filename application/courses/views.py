from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required 
from application.courses.models import Course 
from application.courses.forms import CourseForm

@app.route("/courses", methods=["GET"])
@login_required
def courses_index():
    return render_template("courses/list.html", coursecompletions = Course.query.filter(Course.student_id == current_user.id))

@app.route("/courses/new/")
@login_required
def courses_form():
    return render_template("courses/new.html", form = CourseForm())

@app.route("/courses/<coursecompletion_id>/", methods=["POST"])
@login_required
def courses_set_done(coursecompletion_id):
    course = Course.query.get(student_id)
    course.coursenumber = 0
    db.session().commit()

    return redirect(url_for("courses_index"))

@app.route("/courses/", methods=["POST"])
@login_required(role="USER")
def courses_create():
    form = CourseForm(request.form)

    if not form.validate():
        return render_template("courses/new.html", form = form)

    course = Course(form.name.data)
    course.coursenumber = form.number.data
    course.student_id = current_user.id

    db.session().add(course)
    db.session().commit()
  
    return redirect(url_for("courses_index"))

@app.route("/courses/del/<coursecompletion_id>", methods=["POST"])
@login_required(role="USER")
def courses_delete(coursecompletion_id):
    course = Course.query.get(course_id)
    db.session().delete(course)
    db.session().commit()

    return redirect(url_for("courses_index"))
