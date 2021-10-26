from flask import Flask
from flask_restful import Resource, Api, reqparse
from helper import search_word
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.search_engine
ham = db.ham

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('text')


class Search(Resource):
    def get(self):
        pass

    def post(self):
        args = parser.parse_args()
        text = args['text']
        print(text, type(text))
        words = text.split()
        data = ham.find()
        print(data)
        text, title = search_word(data, words)
        print(text, title)
        return {
            'title': title,
            'text': text
        }



api.add_resource(Search, "/search")
if __name__ == '__main__':
    app.run(debug=True)
