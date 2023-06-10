import torch

from flask import Flask
from flask_cors import CORS, cross_origin

from model.Model import Model

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
@cross_origin()
def root():
    return "Hello World"


if __name__ == "__main__":
    model = Model()
    model.load_state_dict(torch.load("model/data/model.pth"))
    model.eval()

    app.run(debug=True)
