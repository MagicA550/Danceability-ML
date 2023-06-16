import numpy as np
import pandas as pd

from typing import List


class GenreStore:
    """ A store which maps Spotify genre names to a unique numeric identifier. """

    genres: List[str] = []
    """ A List containing the genres added to the store; the index is their unique identifier. """

    def __init__(self, csv_file: str):
        file = pd.read_csv(csv_file)

        for genre in sorted(np.unique(file["track_genre"])):
            self.genres.append(str(genre).lower())

    def get(self, genre: str) -> int:
        """ Gets the identifier of a genre. """
        return self.genres.index(genre)

    def __getitem__(self, idx: int) -> str:
        """ Returns the genre with the identifier given. """
        return self.genres[idx]

    def __contains__(self, genre: str) -> bool:
        """ Determines whether the genre string given is contained within the store. """
        return genre in self.genres

    def __str__(self) -> str:
        """ Converts the store's list to a string. """
        return str(self.genres)
