from src.models.base import BaseModel
from src.extensions import db


class RevokedToken(BaseModel):
    """Generates revoked token table"""

    id = db.Column(db.Integer, primary_key=True, index=True)
    revoked_token = db.Column(db.String(120), nullable=False)
    token_type = db.Column(db.String(16), nullable=False)

    def __repr__(self):
        return "<id: revoked_token: {} >".format(self.revoked_token)

    @classmethod
    def is_token_blocklisted(cls, token):
        """Checks if token is block listed"""
        token = cls.query.filter_by(revoked_token=str(token)).scalar()
        return token is not None
