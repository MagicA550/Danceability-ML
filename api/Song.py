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


class SongConversionException(Exception):
    """ Raised when we attempt to convert an invalid dict to a Song. """
    pass


def to_song(data: dict) -> Song:
    """ Converts a dictionary to a Song object. """

    try:
        return Song(**{field: data[field] for field in data})
    except (AttributeError, TypeError, KeyError):
        raise SongConversionException()
