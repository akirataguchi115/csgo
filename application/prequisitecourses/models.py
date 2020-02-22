from application import db
from application.models import Base

class Prequisitecourse(Base):
    
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    prequisite_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

    def __init__(self, grade):
        self.grade = grade
