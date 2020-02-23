from application import db
from application.models import Base

class Coursecompletion(Base):
   
    startingdate = db.Column(db.Date, nullable=False)
    completiondate = db.Column(db.Date, nullable=False)
    grade = db.Column(db.Integer, nullable=False)

    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

    def __init__(self, grade):
        self.grade = grade
