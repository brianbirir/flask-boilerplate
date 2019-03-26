import os
from flask import Flask
from dotenv import load_dotenv

# load dot env
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
dot_env_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dot_env_path)

# database configs
database_uri = os.getenv('DATABASE_URI')

# initialize Flask app
app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')


# home page route
@app.route('/')
def home():
    return 'Welcome home!'
