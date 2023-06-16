from dataclasses import dataclass


@dataclass
class Song:
    """ A representation of a single song for use in JSON-based requests. """

    acousticness: float
    danceability: float
    duration_ms: int
    energy: float
    explicit: bool
    instrumentalness: float
    key: int
    liveness: float
    loudness: float
    mode: int
    popularity: int
    speechiness: float
    tempo: float
    time_signature: int
    valence: float
