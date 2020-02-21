# Architecture of the database

## Database tables

### Student
Attributes: id, name, student number

### Course
Attributes: id, name, points(ECTS)

### Coursecompletion
Attributes: id, course_id, student_id, startingdate, completiondate, grade

## Database diagram
![Database diagram](https://github.com/akirataguchi115/csgo/blob/master/documentation/csgo_tietokantakaavio.png)
The diagram was made with [draw.io](https://draw.io)
## Normalization
## CREATE TABLE -clauses
```SQL
CREATE TABLE Student (
  id INTEGER
  username VARCHAR(64)
  password VARCHAR(64)
  studentnumber INTEGER
  name VARCHAR(64)
  PRIMARY KEY (id)
);

CREATE TABLE Course (
  id INTEGER
  name VARCHAR(64)
  points INTEGER
  PRIMARY KEY (id)
);

CREATE TABLE Coursecompletion (
  startingdate DATE
  completiondate DATE
  grade INTEGER
  FOREIGN KEY (student_id)
    REFERENCES Student(id)
  FOREIGN KEY (course_id)
    REFERENCES Course(id)
);
```
