from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField, SelectField 

class CoursecompletionForm(FlaskForm):
    # startingdate = DateField("Starting Date")
    # completiondate = DateField("Completion Date")
    course_id = SelectField("Course", coerce=int)
    grade = IntegerField("Course grade")

    class Meta:
        csrf = False
