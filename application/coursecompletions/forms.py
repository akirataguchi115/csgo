from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField, SelectField, DateField 

class CoursecompletionForm(FlaskForm):
    startingdate = DateField("Starting Date")
    completiondate = DateField("Completion Date")
    course_id = SelectField("Course", coerce=int)
    grade = IntegerField("Course grade", [validators.NumberRange(min=1, max=5, message="The scheduled course grade must be between 1 and 5")])

    class Meta:
        csrf = False
