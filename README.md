# Course Scheduler: Graduating On-time
`csgo` is course Scheduler that allows the student to plan one's courses in the way that the soft(or hard) prequisites are met. This way the student can attend courses that are in *topological* order. E.g. If a student schedules themselves a _Database application training project_ with the course _Basics of databases_ that has a completion date later than of the _Database application training project_'s starting date.
The application is live [here](https://csgoplanner.herokuapp.com/). One can test the application from within the Heroku by first registering in the application.
## Documentation
* [Manual](https://github.com/akirataguchi115/csgo/blob/master/documentation/manual.md)
* [Installing / Building (for developers)](https://github.com/akirataguchi115/csgo/blob/master/documentation/installinstructions.md)
* [What's left out](https://github.com/akirataguchi115/csgo/blob/master/documentation/focus.md)
* [User stories](https://github.com/akirataguchi115/csgo/blob/master/documentation/userstories.md)
* [Database structure](https://github.com/akirataguchi115/csgo/blob/master/documentation/architecture.md)
## Entity relations in the Database
![Entity Relation](https://github.com/akirataguchi115/csgo/blob/master/documentation/csgo_tietokantakaavio.png)
The entity relations were made in [draw.io](https://draw.io).

### Implementation / Focus
The `completionDate` is built as an enum (1-4)+completion year referring to study periods during a certain year. The `completionDate` could also be a `Date` type and could simple be compared in days f.ex.
```
Course: startingDate=13-01-2020
(prequisite)Course: completionDate=12-01-2020
```
In this case the prequisites area met as the diff `Course.startingDate - (prequisite)Course.completionDate >= 1 days`. This way the `completionDate` attribute doesn't become a problem as an attribute.
The `PrequisiteCourse` implementation will most likely be the most complicated part of this project.
## Other
![Achecker passed](https://github.com/akirataguchi115/csgo/blob/master/documentation/acheck.jpg)
AChecker - The Web Accessibility Checker found no Known problems, Likely Problems or Potential Problems associated with accessibility on Heroku build v53.
