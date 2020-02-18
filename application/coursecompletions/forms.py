from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField 

class CoursecompletionForm(FlaskForm):
    name = StringField("Course name", [validators.Length(min=2)])
    number = IntegerField("Course starting date")

    class Meta:
        csrf = False
