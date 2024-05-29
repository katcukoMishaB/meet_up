from app import app, db 
from flask import jsonify
from flask_restful import Resource, request
from models.user_model import User
from models.encounter_model import UserEncounter
from datetime import datetime, timedelta

class SkipController(Resource):
    @app.route('/skip-user', methods=['POST'])
    def skip_user():
        data = request.get_json()
        print(data)
        user_id = data.get('user_id')
        encountered_user_id = data.get('encountered_user_id')

        if not user_id or not encountered_user_id:
            return jsonify({'message': 'User ID and Skipped User ID are required'}), 400

        encounter = UserEncounter.query.filter_by(user_id=user_id, encountered_user_id=encountered_user_id).first()
        if encounter:
            encounter.skipped = True
            encounter.last_encountered = datetime.utcnow()
        else:
            encounter = UserEncounter(
                user_id=user_id,
                encountered_user_id=encountered_user_id,
                skipped=True,
                last_encountered=datetime.utcnow()
            )
            db.session.add(encounter)

        db.session.commit()
        return jsonify({'message': 'User skipped successfully'}), 200

    @app.route('/delete-encounters', methods=['DELETE'])
    def cleanup_encounters():
        threshold_date = datetime.utcnow() - timedelta(minutes=1)  
        UserEncounter.query.filter(UserEncounter.last_encountered < threshold_date).delete()
        db.session.commit()
        return jsonify({'message': 'Old encounters cleaned up successfully'}), 200