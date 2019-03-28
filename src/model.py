from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from passlib.hash import pbkdf2_sha256

db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def save_to_db(self):
        """

        :return: none

        This function saves data to the database
        """
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        """

        :return: none

        This function deletes data from the database
        """
        db.session.delete(self)
        db.session.commit()


class UserModel(BaseModel):

    __tablename__ = 'Users'
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)

    @staticmethod
    def generate_hash(password):
        return pbkdf2_sha256.hash(password)

    @staticmethod
    def verify_hash(password, password_hash):
        return pbkdf2_sha256.verify(password, password_hash)
