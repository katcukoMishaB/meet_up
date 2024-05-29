from app import db
from .user_model import User
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy import JSON
class Tags(db.Model):

    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', name='fk_user_id'), index=True)
    description = db.Column(db.String, index=True)
    tags = db.Column(MutableList.as_mutable(JSON))

    user = db.relationship('User', back_populates='tags')   