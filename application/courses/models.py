from application import db
from application.models import Base

class Course(Base):
    
    name = db.Column(db.String(144), nullable=False)
    points = db.Column(db.Integer, nullable=False)

    coursecompletions = db.relationship("Coursecompletion", backref='course', lazy=True)

    def __init__(self, name):
        self.name = name
        self.points = 0
