# User stories
* As a user I want to schedule my courses that I'm going to attend throughout the degree
  * As an user I have a plan of my own stored in the database
  * The software knows about the prequisites of the courses
    * The database table is joined *recursively* to another similiar table
  * The software ought to warn the end-user if he/she takes wrong action(plan courses when the student doesn't meet the prequisites for)
* As an admin I want to able to modify the courses' prequisite information
  * There won't be no admin role with elevated permissions so the courses(and their prequisites) must be input to the databases manually using bare `SQL` commands.
* As a user I want to be able to see my current degree I'm working on
  * Degree shall have the relevant attributes the student might find handy
