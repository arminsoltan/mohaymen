from logging import debug
from re import search
from flask import Flask
from flask_restful import Resource, Api, reqparse
from pymongo import MongoClient
from helper import search_word

client = MongoClient("localhost", 27017)
db = client.search_engine
ham = db.ham

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('text')

class Search(Resource):
    def post(self):
        args = parser.parse_args()
        client_text = args['text']
        data = ham.find()
        search_word(data, client_text)
        pass        

api.add_resource(Search, '/search')

if __name__ == "__main__":
    app.run(debug=True)


