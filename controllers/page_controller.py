from app import app
from flask import render_template
from flask_restful import Resource


class PageConroller(Resource):
    @staticmethod
    @app.route('/', methods=['GET'])
    def get_main_page():
        return render_template('index.html')