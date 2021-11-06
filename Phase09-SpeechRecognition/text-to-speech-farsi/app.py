from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_pymongo import PyMongo
import wave
from pydub import AudioSegment
from io import BytesIO
import numpy as np
import requests
from pymongo import MongoClient
from scipy.io.wavfile import read, write

app = Flask(__name__)
api = Api(app)

client = MongoClient("localhost", 27017)
db = client.speech_recognition
ham = db.ham

parser = reqparse.RequestParser()
parser.add_argument('text')


def retrieve_sound(sentence):
    words = sentence.strip().split()
    print(words)
    combined_sound = AudioSegment.empty()
    word_sounds = ham.find()
    for word in words:
        for sound in word_sounds:
            if word == sound["text"]:
                try:
                    print(word, sound["text"])
                    word_sound = AudioSegment.from_wav("data/{}.wav".format(sound["index"]), "rb")
                    print(word_sound, type(word_sound))
                    combined_sound += word_sound
                    break
                except Exception as err:
                    print(err)
    combined_sound.export("output.wav", format="wav")
    return AudioSegment.from_wav("output.wav")


class Convertor(Resource):
    def post(self):
        args = parser.parse_args()
        text = args["text"]
        retrieve_sound(text)
        return 200


api.add_resource(Convertor, "/convertor")


def transfer_sounds_to_DB():
    text_file = open("data/words.txt", "r")
    for sentence in text_file:
        words = sentence.split()
        if len(words) != 2:
            continue
        dic = {
            'index': words[1],
            'text': words[0]
        }
        ham.insert_one(dic)


if __name__ == "__main__":
    transfer_sounds_to_DB()
    app.run()
