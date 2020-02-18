from application import db
from application.models import Base

from sqlalchemy.sql import text

class Student(Base):
    __tablename__ = "student"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    coursecompletions = db.relationship("Coursecompletion", backref='student', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

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

   # fix @staticmethod
    #def find_users_with_no_students(done=0):
    #    stmt = text("SELECT Account.id, Account.name FROM Account"
    #                " LEFT JOIN Student ON Student.account_id = Account.id"
    #                " WHERE (Student.studentnumber IS null OR Student.studentnumber = :done)"
    #                " GROUP BY Account.id"
    #                " HAVING COUNT(Student.id) = 0").params(done=done)
   #     res = db.engine.execute(stmt)

   #     response = []
   #     for row in res:
   #         response.append({"id":row[0], "name":row[1]})

   #     return response
