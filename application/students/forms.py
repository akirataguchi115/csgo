from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, IntegerField

class LoginForm(FlaskForm):
    username = StringField("Username", render_kw={'autofocus':True})
    password = PasswordField("Password")

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    username = StringField("New username")
    password = PasswordField("New password")
    name = StringField("Name")
    studentnumber = IntegerField("Student number")
   
    class Meta:
        csrf = False
        
class UpdateForm(FlaskForm):
    passwordagain = PasswordField("Old password")
    password = PasswordField("New password")
    name = StringField("New Name")
   
    class Meta:
        csrf = False
