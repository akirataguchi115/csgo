# How to install
## Cloning the repo
`git clone` the repository to your desired directory [like so](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository). 
## Installing the `python` requirements
Install all the Python-project requirements with `pip install -r requirements.txt`(python and pip must also be installed).
## Installing venv
`python3 -m venv venv`
## Running locally
In the root of the project run `source venv/bin/activate` to activate the development environment. Run `python run.py`. The application is now running in f.ex. `localhost:5000` depending on the PC's configurations in the web browser like so:
![Running in port 5000](https://github.com/akirataguchi115/csgo/blob/master/documentation/likeso.png)
## Running on Heroku
Install  [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) and log in with the corresponding instructions. While in your development environment(venv) run `heroku create thenameoftheherokuappyouwant` then `git remote add heroku https://git.heroku.com/thenameoftheherokuappyouwant.git`(assuming you have git installed).
After that just `git add .`, `git commit -m "yourcommitmessagehere"` and `git push heroku master`. The application is now running in public on [https://thenameoftheherokuappyouwant.herokuapp.com/](https://thenameoftheherokuappyouwant.herokuapp.com/).
