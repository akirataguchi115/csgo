# Architecture of the database

## Database tables

### Student
Attributes: id, name, student number

### Course
Attributes: id, name, points(ECTS)

### Coursecompletion
Attributes: id, course_id, student_id, startingdate, completiondate, grade

### Prequisitecourse
Attributes: id, course_id, prequisite_id

## Database diagram
![Database diagram](https://github.com/akirataguchi115/csgo/blob/master/documentation/csgo_tietokantakaavio.png)
The diagram was made with [draw.io](https://draw.io)
## Normalization
### Satisfying the 1NF
1. There are no lists in the columns
1. There are no repeating groups
1. Each column has only one type (provided by the SQLite or PostgreSQL)
1. Each column has a unique name
1. The order of the columns doesn't affect the application
1. There are no duplicate rows in the database due to every insertion having an unique id within the table.
1. The order of the rows doesn't affect the application
### Satisfying the 2NF
The tables' columns are functionally dependent on **one** Primary Key although the student id's are technically unique the application the database itself doesn't rely on the uniqueness of the student numbers (although it definetily should).
### Satisfying the 3NF
The tables' columns are transitively dependent on the Primary Key, alas the database is not in the third normal form. This is because the student's name and password could be obtained just by knowing the username. This was denormalized so that the database could be displayed more easily in the database diagram.
## CREATE TABLE -clauses
```SQL
CREATE TABLE Student (
  id INTEGER
  username VARCHAR(128)
  password VARCHAR(128)
  studentnumber INTEGER
  name VARCHAR(128)
  PRIMARY KEY (id)
);

CREATE TABLE Course (
  id INTEGER
  name VARCHAR(128)
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

CREATE TABLE Prequisitecourse (
  FOREIGN KEY (course_id)
    REFERENCES Course(id)
  FOREIGN KEY (prequisite_id)
    REFERENCES Course(id)
);
```
