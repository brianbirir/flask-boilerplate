from datetime import datetime

from passlib.hash import pbkdf2_sha256

from src.models.base import BaseModel
from src.extensions import db


class User(BaseModel):
    """User table representation"""

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    confirmed = db.Column(db.Boolean, nullable=False, server_default="false")
    is_disabled = db.Column(db.Boolean, nullable=False)
    last_login_date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow())
    roles = db.relationship("Role", secondary="users_roles")

    def get_id(self):
        return self.user_id

    def __repr__(self):
        return f"<User {self.email}>"

    @staticmethod
    def generate_hash(password):
        """Generates a password hash from raw password"""
        return pbkdf2_sha256.hash(password)

    @staticmethod
    def verify_hash(password, password_hash):
        """Verifies provided password against hashed password"""
        return pbkdf2_sha256.verify(password, password_hash)

    @classmethod
    def find_by_email(cls, email):
        """Returns by email"""
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_user_id(cls, user_id):
        """Returns user by user id"""
        return cls.query.filter_by(id=user_id).first()

    @classmethod
    def get_all_users(cls):
        """Returns all users"""
        return cls.query.all()


class Role(BaseModel):
    role_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Role {self.name}>"

    @classmethod
    def check_for_roles(cls):
        """Checks if roles are available"""
        return cls.query.first()


user_role_association_table = db.Table(
    "users_roles",
    db.Model.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("user.user_id"), primary_key=True),
    db.Column("role_id", db.Integer, db.ForeignKey("role.role_id"), primary_key=True),
)
