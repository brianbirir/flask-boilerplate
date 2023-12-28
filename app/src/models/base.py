from datetime import datetime

from src.extensions import db


class BaseModel(db.Model):
    """Generates basic columns and contains base functions for all models

    Args:
        db.Model (class): A declarative base for declaring models.

    """

    __abstract__ = True
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    created_by = db.Column(db.String(120), nullable=True)
    modified_by = db.Column(db.String(120), nullable=True)

    def save(self):
        """Writes data to the database"""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Deletes data from the database"""
        db.session.delete(self)
        db.session.commit()
