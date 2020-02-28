from application import db
from application.models import Base
from flask_login import current_user
from sqlalchemy.sql import text
from datetime import datetime

class Coursecompletion(Base):
   
    startingdate = db.Column(db.Date, nullable=False)
    completiondate = db.Column(db.Date, nullable=False)
    grade = db.Column(db.Integer, nullable=False)

    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

    def __init__(self, grade):
        self.grade = grade

    @staticmethod
    def list_courses():
        stmt = text("SELECT Course.name, Coursecompletion.grade, Coursecompletion.startingdate, Coursecompletion.completiondate, Coursecompletion.id, Course.id FROM Course"
                " LEFT JOIN Coursecompletion ON Course.id = Coursecompletion.course_id"
                " WHERE Coursecompletion.student_id = :student_id").params(student_id=current_user.id)
        coursecompletions = []
        result = db.engine.execute(stmt)
        for row in result:
            stmt = text("SELECT Coursecompletion.completiondate"
                        " FROM Coursecompletion"
                        " LEFT JOIN Prequisitecourse ON Prequisitecourse.prequisite_id = Coursecompletion.course_id"
                        " WHERE Prequisitecourse.course_id = :courseid"
                        " AND Coursecompletion.student_id = :student_id").params(courseid=row[5],student_id=current_user.id)
            result = db.engine.execute(stmt)
            prequisitesmeet = True
            for nextrow in result:
                if row[2] < nextrow[0]:
                        prequisitesmeet = False
                        break
            coursecompletions.append({"name":row[0], "grade":row[1], "startingdate":row[2], "completiondate":row[3], "id":row[4], "prequisitesmeet":prequisitesmeet})

        return coursecompletions

    @staticmethod
    def count_completions():
        stmt = text("SELECT COUNT(Coursecompletion.grade) FROM Coursecompletion"
                    " WHERE Coursecompletion.student_id = :student_id").params(student_id=current_user.id)
        res = db.engine.execute(stmt)
        result = 0
        for row in res:
            result = row[0]
        
        return result

    @staticmethod
    def grade_average():
        stmt = text("SELECT ROUND(AVG(Coursecompletion.grade),2)" 
                    " FROM Coursecompletion"
                    " WHERE Coursecompletion.student_id = :student_id").params(student_id=current_user.id)
        res = db.engine.execute(stmt)
        result = 0
        for row in res:
            result = row[0]
        return result
