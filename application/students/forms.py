from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField

class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    username = StringField("New username")
    password = PasswordField("New password")
   
    class Meta:
        csrf = False
