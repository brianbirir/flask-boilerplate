# Flask RESTFul Boilerplate
A Flask boiler plate for kicking off Flask RESTful related development projects. The key features of this boilerplate include:

* ORM implementation using `Flask-SQLalchemy` with connection to any preferred database technology
* RESTful implementation using `Flask-Restful` module
* Implementation of resource authentication using JWTs (JSON Web Tokens). JWTs usage has been implemented using `pyjwts` library
* Implementation of database migrations using `Flask-Migrate` and Alembic. A base and user model have been added in the `model.py` module to allow the creation of the users table in a designated database
* Unit and functional tests for the above features

Though this boilerplate is the basis of building a RESTFul API application, it can be extended to include user facing web pages through **Jinja2** Templating and Flask views rendering if desired.


## Requirements
* Python 3
* JWTs (JSON Web Tokens) implementation for Python
* Flask and it's dependencies (all defined in the `requirements.txt` file)

## Setup
* Virtualenv - install a Python virual environment i.e. `virtualenv env` and activate it `source env/bin/activate`

* Install Flask and dependencies and add them to `requirements.txt`

```bash
$ pip freeze > requirements.rxt
```
* Install and configure PostgreSQL database. The following commands create a user and a database. The user is then granted access to the database with certain privileges. The user and database names are upto you (also password).

```
create role flask_bp with login password 'flask_bp';

alter role flask_bp createdb;

create database flask_bp;

grant all privileges on database flask_bp to flask_bp;

```

## Run Application

### Development Mode:
#### WSGI Server
The application is served using Gunicorn WSGI within the project's root folder. Pass the configuration type as an argument. In this case, the configuration is a module and loaded as an object.

```bash
gunicorn "src:create_app('config.DevelopmentConfig')"
```

However, before the application is executed, there's need to handle database migrations for SQLAlchemy. Flask-Migrate is used to the handle the migration of the database model objects to the PostgrSQL database. The following commands are executed in the shell to carry out the migration:

```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

#### Flask Debug Mode (Local Development Server)
The application can also be run by adding a Flask app entry point module and naming it as desired e.g. `app.py`. Then add the following code to the entry point module. 

```python
from src import create_app


if __name__ == "__main__":
    """
    This module should only be used for development when running this application using the Flask web server.
    Running this is in production is not recommended hence look at other production level WSGI like Gunicorn
    """
    create_app('config.DevelopmentConfig').run('0.0.0.0')
```

Then run the app: `python app.py`

You could also check the quick start guide in the [Flask documentation](http://flask.pocoo.org/docs/1.0/quickstart/#debug-mode) on other methods of running the application using the local development server.

>> **Note one:** Never use the Flask development web server in production. That's one big security risk and it's not scalable.

>> **Note two:** When running this Flask application, ensure the virtual environment is activated.


### Production Mode:
To-Do


## To-Do
* Document sample API using Swagger
* Dockerize - Add capability to run the application using Docker
* ~~Update application configuration input~~
