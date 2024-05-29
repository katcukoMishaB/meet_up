from app import db

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True)
    username = db.Column(db.String(64), index=True, unique=True)
    allows_write_to_pm = db.Column(db.Boolean, index=True)

    tags = db.relationship('Tags', back_populates='user')
    encounters = db.relationship("UserEncounter", back_populates="user")
    