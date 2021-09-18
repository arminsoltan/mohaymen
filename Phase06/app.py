import torch
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from model import LSTM 


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
# parser.add_argument('')
# parser.add
# _

# vocab_size = len(TEXT.vocab) + 1
# output_size = 1
# embedding_dim = 400
# hidden_dim = 256
# n_layers = 2
# model = LSTM(vocab_size, output_size, embedding_dim, hidden_dim, n_layers)

net = torch.load("LSTM.pt", map_location=torch.device('cpu'))
class SadHappiness(Resource):
    def get(self):
        return {"response": "In this model we aim to categorize sad or happiness of text"}
    
    def post(self):
        text = request.json["text"]
        print(net)
        # val_h = net.init_hidden(64)
        # val_h = tuple([each.data for each in val_h])
        output, a = net(text, None)
        print(output)
        print("\n \n \n")

api.add_resource(SadHappiness, '/')

if __name__ == "__main__":
    app.run(debug=True)
