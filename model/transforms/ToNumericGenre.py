from model.stores.GenreStore import GenreStore

# Create a universal GenreStore for use within the Transformer and elsewhere.
genre_store = GenreStore()


class ToNumericGenre(object):
    """ Converts a Spotify genre to a unique numeric representation. """

    def __call__(self, genre: str) -> int:
        return genre_store.add(genre)
