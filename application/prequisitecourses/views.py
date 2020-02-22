from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required 
from application.coursecompletions.models import Coursecompletion 
from application.coursecompletions.forms import CoursecompletionForm

from application.courses.models import Course
from application.courses.forms import CourseForm

from sqlalchemy.sql import text


