from flask import Blueprint, request

from api.Endpoint import model
from api.Song import to_song

genre_blueprint = Blueprint("genre", __name__)


@genre_blueprint.route("/genre", methods=["POST"])
def genre():
    content = request.json
    song = to_song(content)
    return [model.predict(song)]
