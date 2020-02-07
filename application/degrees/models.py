from application import db
from application.models import Base

from sqlalchemy.sql import text

class Degree(Base):

    points = db.Column(db.Integer, nullable=False)
    university = db.Column(db.String(144), nullable=False)

    students = db.relationship("StudentDegree", backref='degree', lazy=True)

    def __init__(points, university ) 
        self.points = points
        self.university = university

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
