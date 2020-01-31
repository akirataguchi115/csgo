from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class StudentForm(FlaskForm):
    name = StringField("Student name", [validators.Length(min=2)])
    number = IntegerField("Student number")

    class Meta:
        csrf = False
