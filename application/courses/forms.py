from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class CourseForm(FlaskForm):
    name = StringField("Course name", [validators.Length(min=2)])
    number = IntegerField("Course number")

    class Meta:
        csrf = False
