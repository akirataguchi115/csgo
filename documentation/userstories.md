# User stories
Functionality | Implemented
------------ | -------------
As a user I can list out my scheduled courses | X
The software knows about the prequisites of the courses (warns if prequisites are not met)| X
The software ought to warn the end-user if he/she takes wrong action(plan courses when the student doesn't meet the prequisites for) | _merged with the former one_
As a user I want to see how many courses I have scheduled | X
As a user I want to see what is the average grade of my scheduled courses | X

## Listing the scheduled courses:
```SQL
"SELECT Course.name, Coursecompletion.grade, Coursecompletion.startingdate, Coursecompletion.completiondate, Coursecompletion.id, Course.id"
                " FROM Course"
                " LEFT JOIN Coursecompletion ON Course.id = Coursecompletion.course_id"
                " WHERE Coursecompletion.student_id = :student_id"
```
where the :student_id is the id of the current user.

## Seeing if prequisites are met
```SQL
"SELECT Coursecompletion.completiondate"
                        " FROM Coursecompletion"
                        " LEFT JOIN Prequisitecourse ON Prequisitecourse.prequisite_id = Coursecompletion.course_id"
                        " WHERE Prequisitecourse.course_id = :courseid"
                        " AND Coursecompletion.student_id = :student_id"
```
where the :courseid is the id of the currently observed course (received from the first `SQL` clause) and the :student_id being again the id of the current user. By comparing the course's and prequisite courses' completion and starting dates (in our case with Python) we can see if the scheduling is done correctly according to the prequisites.

## Counting the amount of scheduled courses
```SQL
"SELECT COUNT(Coursecompletion.grade) FROM Coursecompletion"
                    " WHERE Coursecompletion.student_id = :student_id"
```
where the :student_id is once again the id of the currently logged in user.

## Getting the the average of the scheduled courses' grades
```SQL
"SELECT ROUND(AVG(Coursecompletion.grade),2)" 
                    " FROM Coursecompletion"
                    " WHERE Coursecompletion.student_id = :student_id"
```
where the :student_id is once again the id of the currently logged in user.

## Other
Other application's database related functionality are implemented with SQLAlchemy(ORM) such as `INSERT` and `DELETE` clauses where as the implementation of `cascade` is the only one not trivial. When a table is marked cascade to some "parent" with right configurations of killing of an orphan causes the ORM to execute a handful of `DELETE` clauses to the database where each insertion asocciated with the soon-to-be-deleted parent will also be `DELETE`d from the database.
