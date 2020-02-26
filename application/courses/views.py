from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required 
from application.courses.models import Course 
from application.courses.forms import CourseForm

