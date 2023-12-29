import os
from datetime import timedelta

from dotenv import load_dotenv


class Config:
    """Loads configurations from environment variables"""
    env_file_path = os.path.dirname((os.path.abspath(__file__)))
    env_file = env_file_path + "/" + "env_configs/.env"
    load_dotenv(dotenv_path=env_file)

    # jwt
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_BLACKLIST_ENABLED = os.getenv("JWT_BLACKLIST_ENABLED")
    JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

    # flask
    SERVER_NAME = os.getenv("SERVER_NAME")
    DEBUG = False
    TESTING = False

    # database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": Config,
}
