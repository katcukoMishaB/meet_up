from datetime import datetime
from app import db

class UserEncounter(db.Model):
    __tablename__ = "user_encounter"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', name='fk_encounter_id'), nullable=False)
    encountered_user_id = db.Column(db.Integer, nullable=False)
    skipped = db.Column(db.Boolean, default=False)
    last_encountered = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', back_populates='encounters')
    
 
