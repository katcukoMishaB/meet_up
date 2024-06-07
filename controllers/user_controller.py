from app import app, db
from flask import jsonify
from flask_restful import Resource, request
from models.user_model import User
from models.tags_model import Tags

from flask_cors import CORS
CORS(app)


class UserController(Resource):
    @app.route('/send-user-data', methods=['POST'])
    def send_user_data():
        data = request.get_json()
        print(data)
        user_id = data.get('id')
        first_name = data.get('first_name')
        username = data.get('username')
        allows_write_to_pm = data.get('allows_write_to_pm')

        if not user_id or not first_name or not username:
            return jsonify({'message': 'User data incomplete'}), 400

        existing_user = User.query.filter_by(id=user_id).first()
        existing_tags = Tags.query.filter_by(user_id=user_id).first()

        if existing_user and existing_user.username != username:
            existing_user.username = username
            db.session.commit()

        if existing_user and existing_tags:
            print('user and tags already in')
            return jsonify({'message': 'User and Tags already exists'}), 200
        
        if existing_user:
            print('user already in')
            return jsonify({'message': 'Tags already exists'}), 200
        
        new_user = User(
            id=user_id,
            first_name=first_name,
            username=username,
            allows_write_to_pm=allows_write_to_pm
        )

        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User added successfully'}), 201
    

