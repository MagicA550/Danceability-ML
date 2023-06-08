class ToLowerCase(object):
    """ Converts a given string to lower case for use in further pre-processing. """

    def __call__(self, genre: str) -> str:
        return genre.lower()
