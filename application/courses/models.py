from application import db
from application.models import Base

class Course(Base):
    
    name = db.Column(db.String(144), nullable=False)
    studentnumber = db.Column(db.Integer, nullable=False)

    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)

    def __init__(self, name):
        self.name = name
        self.studentnumber = 0
