from flask import Flask
from flask_cors import CORS, cross_origin

from api.endpoints.Genre import genre_blueprint
from api.endpoints.Genres import genres_blueprint

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
@cross_origin()
def root():
    return "Hello World"


if __name__ == "__main__":
    app.register_blueprint(genre_blueprint)
    app.register_blueprint(genres_blueprint)

    app.run(debug=True)
