from app import app, db
from flask import jsonify
from flask_restful import Resource, request
from models.tags_model import Tags
from flask_cors import CORS
CORS(app)

class TagsController(Resource):
    @app.route('/send-description-and-options', methods=['POST'])
    def send_description_and_optionts():
        data = request.get_json()
        
        if data is None:
            return jsonify({'message': 'No JSON payload provided'}), 400
        
        user_id = data.get('user_id')
        description = data.get('description')
        tags = data.get('tags')
        
        if not user_id:
            return jsonify({'message': 'User ID is missing'}), 400
        
        if not description:
            return jsonify({'message': 'Description is missing'}), 400
        
        if not tags:
            return jsonify({'message': 'Tags are missing'}), 400
        
        print(f"Received data: {data}")
        
        existing_tags = Tags.query.filter_by(user_id=user_id).first()
        
        if existing_tags:
            existing_tags.description = description
            existing_tags.tags = tags
            db.session.commit()
            return jsonify({'message': 'Tags updated successfully'}), 200
        
        new_tags = Tags(
            user_id=user_id,
            description=description,
            tags=tags
        )
        
        db.session.add(new_tags)
        db.session.commit()
        
        return jsonify({'message': 'Tags added successfully'}), 201



        
    