from application import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    studentnumber = db.Column(db.Integer, nullable=False)

    def __init__(self, name, studentnumber):
        self.name = name
        self.studentnumber = studentnumber
