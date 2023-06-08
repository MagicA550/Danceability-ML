from typing import List


class GenreStore:
    """ A store which maps Spotify genre names to a unique numeric identifier. """

    genres: List[str] = []
    """ A List containing the genres added to the store; the index is their unique identifier. """

    def add(self, genre: str) -> int:
        """ Adds the genre to the store if it hasn't already, returning its new identifier. """
        if genre in self:
            return self.genres.index(genre)

        self.genres.append(genre)
        return len(self.genres) - 1

    def __getitem__(self, idx: int) -> str:
        """ Returns the genre with the identifier given. """
        return self.genres[idx]

    def __contains__(self, genre: str) -> bool:
        """ Determines whether the genre string given is contained within the store. """
        return genre in self.genres

    def __str__(self) -> str:
        """ Converts the store's list to a string. """
        return str(self.genres)
