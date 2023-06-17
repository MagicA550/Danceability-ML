from flask import Blueprint, request

from api.Endpoint import model
from api.Song import to_song

genres_blueprint = Blueprint("genres", __name__)


@genres_blueprint.route("/genres", methods=["POST"])
def genres():
    content = request.json
    songs = [to_song(song) for song in content]
    return model.predict_batch(songs)
