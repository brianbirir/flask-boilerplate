"""Makes Flask third party extensions easily accessible

Helps in avoiding circular imports and the extension object does not initially get bound to the application.
In addition, this applicable for cases where application factories is in use like in this app
"""
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


jwt = JWTManager()
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
