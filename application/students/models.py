from application import db
from application.models import Base

from sqlalchemy.sql import text

class Student(Base):
    __tablename__ = "student"

    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    studentnumber = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(144), nullable=False)

    coursecompletions = db.relationship("Coursecompletion", backref='student', lazy=True, cascade="all, delete-orphan")

    def __init__(self, username, password, name, studentnumber):
        self.username = username
        self.password = password
        self.studentnumber = studentnumber
        self.name = name 

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
    def roles(self):
        return ["USER"]
