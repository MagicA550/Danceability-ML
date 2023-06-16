import os
from os.path import dirname, realpath
from dotenv import dotenv_values


class Environment:
    """ Abstracts the fetching of environment variables. """

    def __init__(self):
        self.path_to_root = "../"

        # Fetch variables in the following hierarchy:
        self._environment = {
            **dotenv_values(f"{self.__get_root_path()}.env.local"),  # first, local environment variables (development).
            **dotenv_values(f"{self.__get_root_path()}.env"),  # then, main environment variables (production).
            **os.environ,  # finally, system environment variables.
        }

    def __get_root_path(self) -> str:
        """ Returns the path to the root directory of the project. """
        return f"{dirname(realpath(__file__))}/{self.path_to_root}"

    def __getitem__(self, var: str):
        """ Returns the environment variable using the key provided, or None if it doesn't exist. """
        return self._environment[var]

    @property
    def spotify_client_id(self) -> str:
        """ The Spotify API client id. """
        return self["SPOTIFY_CLIENT_ID"]

    @property
    def spotify_client_secret(self) -> str:
        """ The Spotify API client secret. """
        return self["SPOTIFY_CLIENT_SECRET"]
