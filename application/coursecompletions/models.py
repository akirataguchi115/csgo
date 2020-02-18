from application import db
from application.models import Base

class Coursecompletion(Base):
    
    name = db.Column(db.String(144), nullable=False)
    startingDate = db.Column(db.Integer, nullable=False)

    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    # course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

    def __init__(self, name):
        self.name = name
        self.startingDate = 0 
