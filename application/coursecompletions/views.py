from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required 
from application.coursecompletions.models import Coursecompletion 
from application.coursecompletions.forms import CoursecompletionForm

from application.courses.models import Course
from application.courses.forms import CourseForm

from sqlalchemy.sql import text


@app.route("/coursecompletions", methods=["GET"])
@login_required
def coursecompletions_index():
    stmt = text("SELECT Course.name, Coursecompletion.grade FROM Course"
                " LEFT JOIN Coursecompletion ON Course.id = Coursecompletion.course_id"
                " WHERE Coursecompletion.student_id = :student_id").params(student_id=current_user.id)
    coursecompletions = []
    result = db.engine.execute(stmt)
    for row in result:
        coursecompletions.append({"name":row[0], "grade":row[1]})

    return render_template("coursecompletions/list.html", coursecompletions=coursecompletions)

@app.route("/coursecompletions/new/")
@login_required
def coursecompletions_form():
    form = CoursecompletionForm()
    courses = Course.query.all()
    course_list = [(course.id, course.name) for course in courses]
    form.course_id.choices = course_list
    return render_template("coursecompletions/new.html", form = form)

@app.route("/coursecompletions/<coursecompletion_id>/", methods=["POST"])
@login_required
def coursecompletions_set_done(coursecompletion_id):
    t = Coursecompletion.query.get(coursecompletion_id)
    t.grade = 0
    db.session().commit()

    return redirect(url_for("coursecompletions_index"))

@app.route("/coursecompletions/", methods=["POST"])
@login_required(role="USER")
def coursecompletions_create():
    form = CoursecompletionForm(request.form)
    courses = Course.query.all()
    course_list = [(course.id, course.name) for course in courses]
    form.course_id.choices = course_list
    print(form.course_id.choices)
    if not form.validate():
        return render_template("coursecompletions/new.html", form = form)

    t = Coursecompletion(form.grade.data)
    t.student_id = current_user.id
    t.course_id = form.course_id.data

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("coursecompletions_index"))

@app.route("/coursecompletions/del/<coursecompletion_id>", methods=["POST"])
@login_required(role="USER")
def coursecompletions_delete(coursecompletion_id):
    t = Coursecompletion.query.get(coursecompletion_id)
    db.session().delete(t)
    db.session().commit()

    return redirect(url_for("coursecompletions_index"))
