from flask import Flask, request
from flask_restful import reqparse, Resource, Api
from main import speech_to_text

app = Flask(__name__)
api = Api(app)


class Convertor(Resource):
    def post(self):
        audio_file = request.files["audio_file"]
        response = speech_to_text(audio_file)
        return {
            'text': response
        }, 200


api.add_resource(Convertor, '/convertor')
if __name__ == "__main__":
    app.run()
