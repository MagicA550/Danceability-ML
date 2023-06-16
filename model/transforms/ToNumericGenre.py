from os.path import dirname, realpath

from model.stores.GenreStore import GenreStore

# Create a universal GenreStore for use within the Transformer and elsewhere.
genre_store = GenreStore(f"{dirname(realpath(__file__))}/../data/dataset.csv")


class ToNumericGenre(object):
    """ Converts a Spotify genre to a unique numeric representation. """

    def __call__(self, genre: str) -> int:
        return genre_store.get(genre)
