from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField, SelectField 

class PrequisitecourseForm(FlaskForm):
    course_id = SelectField("Course", coerce=int)
    prequisite_id = SelectField("Prequisite course", coerce=int)

    class Meta:
        csrf = False
