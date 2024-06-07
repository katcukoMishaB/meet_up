from app import app, db
from flask import jsonify
from flask_restful import Resource, request
from models.user_model import User
from models.tags_model import Tags
from models.encounter_model import UserEncounter
from collections import Counter
from itertools import chain

class MatchController(Resource):
    

    @staticmethod
    def calculate_similarity(tags1, tags2):

        tags1_tuple = tuple(tags1)
        tags2_tuple = tuple(tags2)
        print(tags1_tuple)
        print(tags2_tuple)

        common_tags_count = sum((Counter(tags1_tuple) & Counter(tags2_tuple)).values())
        print(common_tags_count)
        print(max(len(tags1_tuple), len(tags2_tuple)))
        similarity = (common_tags_count / min(len(tags1_tuple), len(tags2_tuple))) * 100
        print(similarity)
        return similarity

    @app.route('/find-matches', methods=['POST'])
    def find_matches():
        data = request.get_json()
        print(data)
        "1188181183"  
        user_id = data.get('id')
        user = User.query.get(user_id)
        if not user:
            return jsonify({'message': 'User not found'}), 404
        user_tags = Tags.query.filter(Tags.user_id == user.id).first()
        user_tags = user_tags.tags
        if not user_tags:
            return jsonify({'message': 'User has no tags'}), 400
        print(user_tags)

        matches = []
        users = User.query.filter(User.id != user_id).all()
        print(users)
        for potential_match in users:
            check_encounter = UserEncounter.query.filter(UserEncounter.encountered_user_id == potential_match.id).first()
            print(check_encounter)
            if check_encounter is not None and check_encounter.skipped == 1:
                continue
            potential_match_tag = Tags.query.filter(Tags.user_id == potential_match.id).first()
            potential_match_description = potential_match_tag.description
            print(potential_match)
            potential_match_tags = potential_match_tag.tags
            print(potential_match_tags)
            
            similarity = MatchController.calculate_similarity(user_tags, potential_match_tags)

            if similarity > 49:
                matches.append({
                    'encountered_user_id': potential_match.id,
                    'encountered_username': potential_match.username,
                    'similarity': similarity,
                    'description': potential_match_description,
                    'tags': potential_match_tags
                })

        return jsonify({'matches': matches}), 200
    
        """set1, set2 = set(user_tags), set(potential_match_tags)
            intersection = len(set1.intersection(set2))
            union = len(set1.union(set2))
            similarity = (intersection / union) * 100 if union > 0 else 0

            if similarity > 49:
                matches.append({
                    'user_id': potential_match.id,
                    'similarity': similarity,
                    'description': potential_match.tags.description,
                    'tags': potential_match_tags
                })

        return jsonify({'matches': matches}), 200
"""
    
    """    @app.route('/find-matches', methods=['GET'])
    def find_matches():
        user_id = "1188181183"
        if not user_id:
            return jsonify({'message': 'User ID is required'}), 400

        user = User.query.get(user_id)
        print(user)
        if not user:
            return jsonify({'message': 'User not found'}), 404

        user_tags = [tag.tags for tag in user.tags] if user.tags else []  # Получаем теги пользователя из связанной таблицы
        if not user_tags:
            return jsonify({'message': 'User has no tags'}), 400
        print(user_tags)
        matches = []
        users = User.query.filter(User.id != user_id).all()
        print(users)
        for potential_match in users:
            potential_match_tags = [tag.tags for tag in potential_match.tags] 
            if potential_match.tags 
            else []  
            print(potential_match_tags)
            set1, set2 = set(user_tags), set(potential_match_tags)
            intersection = len(set1.intersection(set2))
            union = len(set1.union(set2))
            similarity = (intersection / union) * 100 if union > 0 else 0

            if similarity > 49:
                matches.append({
                    'user_id': potential_match.id,
                    'similarity': similarity,
                    'description': potential_match.tags.description,
                    'tags': potential_match_tags
                })

        return jsonify({'matches': matches}), 200"""