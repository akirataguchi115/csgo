# Course Scheduler: Graduating On-time
`csgo` is course Scheduler that allows the student to plan one's courses in the way that the soft(or hard) prequisites are met. This way the student can attend courses that are in *topological* order.
The application is live [here](https://csgoplanner.herokuapp.com/). One can log in with the test account with the username `test` and the password `admin` or one can create their own ones from within the site.
## Functions
The course database table has a `completionDate` attribute and 0...n prequisite `Course`s. These `Course`s are joined to the prequisite `Course` with a join table(see the database diagram below).
[User stories](https://github.com/akirataguchi115/csgo/blob/master/documentation/userstories.md) can be read here.
## Entity relations in the Database
![Entity Relation](https://github.com/akirataguchi115/csgo/blob/master/documentation/csgo_tietokantakaavio.png)
The entity relations were made in [draw.io](https://draw.io).

### Implementation
#### What's the focus
The `completionDate` is built as an enum (1-4)+completion year referring to study periods during a certain year. The `completionDate` could also be a `Date` type and could simple be compared in days f.ex.
```
Course: startingDate=13-01-2020
(prequisite)Course: completionDate=12-01-2020
```
In this case the prequisites area met as the diff `Course.startingDate - (prequisite)Course.completionDate >= 1 days`. This way the `completionDate` attribute doesn't become a problem as an attribute.
The `PrequisiteCourse` implementation will most likely be the most complicated part of this project.
#### What's left out
-
