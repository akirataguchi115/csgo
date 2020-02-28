from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, IntegerField, validators

class LoginForm(FlaskForm):
    username = StringField("Username", render_kw={'autofocus':True})
    password = PasswordField("Password")

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    username = StringField("New username", [validators.Length(min=3, max=40, message="Username's length must be between 3 and 40")], render_kw={'autofocus':True})
    password = PasswordField("New password", [validators.Length(min=3, max=40, message="Password's length must be between 3 and 40")])
    name = StringField("Name", [validators.Length(min=3, max=40, message="Name's length must be between 3 and 40")])
    studentnumber = IntegerField("Student number", [validators.NumberRange(min=1, max=1000000000, message="Student number must be in format of 0xx xxx xxx (without spaces where x is a number)")])
   
    class Meta:
        csrf = False
        
class UpdateForm(FlaskForm):
    passwordagain = PasswordField("Old password", [validators.Length(min=3, max=40, message="Password's length must be between 3 and 40")], render_kw={'autofocus':True})
    password = PasswordField("New password", [validators.Length(min=3, max=40, message="Password's length must be between 3 and 40")])
    name = StringField("New Name", [validators.Length(min=3, max=40, message="Name's length must be between 3 and 40")])
   
    class Meta:
        csrf = False
