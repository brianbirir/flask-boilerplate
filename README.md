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
* dot env file of which can be derived from `.env.sample`

## Dot Env
The dot env file contains environment variables used to run the application where required. 

* Create the dot env file from `env.sample` and save as `.env`
* The file should contain the following, however, this should not be used in production:

```
DATABASE_URI=postgresql://api_user:BbYjg7wY@database:5432/api_db
SECRET_KEY=\xcf\x92W\x88w\x85s\xebiE\xfe\x13\xb9\x92\xe3\xee
SQLALCHEMY_TRACK_MODIFICATIONS=False

```
* The `SECRET_KEY` can be generated using the `urandom()` function from Python `os` standard library:

```
import os
os.urandom(24)
```

## Setup (without Containers)
* Virtualenv - install a Python virual environment i.e. `virtualenv env` and activate it `source env/bin/activate`. Virtualenv can be excluded for Docker deployment during development since we'll be utilizing containers to deploy the application.

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

## Setup (with Docker Containers)
In this section, unlike the previous one, entails automation with use of Docker to carry out containerization. The use of Docker during developement reduces the time and effort it will take to setup and run the application. 

The `Dockerfile` and `docker-compose.yml` files inside the `docker` folder contain configurations to automate the deployment of the application. `docker-compose` is used throught the management of the docker containers.

>> Ensure Docker is installed in your development environment before continuing.

### Steps to Setup with Docker
* Clone the repository and change to the project folder
* Run the following command within the project root to build the docker images:

```bash
docker-compose -f docker/docker-compose.yml build --no-cache
```

* Then create and run the containers from the newly created containers

```bash
docker-compose -f docker/docker-compose.yml up
```

The Flask web application should now be accessible. Since it's a API driven application, make use of tools such as `curl`, PostMan or Insomnia to call the following end point:

`GET /api/test`

The output will be a 200 HTTP response in JSON format to confirm the application is up and running:

`curl -v http://localhost:8000/api/test`

```bash
*   Trying ::1...
* TCP_NODELAY set
* Connected to localhost (::1) port 8000 (#0)
> GET /api/test HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/7.54.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Server: gunicorn/19.9.0
< Date: Mon, 13 May 2019 12:28:36 GMT
< Connection: close
< Content-Type: application/json
< Content-Length: 53
<
{
    "message": "The Flask API web service works"
}
* Closing connection 0

```
Of note, is that the Flask application within the Docker container is run using Gunicorn. In a future implementation, there will be an option to run the docker containers using either `PRODUCTION` or `DEVELOPMENT` mode. 

With development mode, the application will use the inbuilt Flask web server in order to get debugging messages and the production mode will use Gunicorn.

>> A future automation implementation will see the use of 


## To-Do
* Document sample API using Swagger
* Dockerize - Add capability to run the application using Docker
* ~~Update application configuration input~~
