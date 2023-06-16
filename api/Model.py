from dataclasses import asdict
from os.path import dirname, realpath

import pandas as pd
import torch
from typing import List

from torch import load, Tensor

from api.Song import Song
from model.Model import Model as PyTorchModel
from model.SpotifyTracksDataset import dataset
from model.transforms.ToNumericGenre import genre_store


class Model:
    """ An abstraction of the PyTorch model defined elsewhere to allow for simple predictions to be made directly
    from API requests."""

    def __init__(self):
        self.model = PyTorchModel()
        self.model.load_state_dict(load(f"{dirname(realpath(__file__))}/../model/data/model.pth"))
        self.model.eval()

    def predict(self, features: Song) -> str:
        """ Predicts the genre of a single song. """
        return self.predict_batch([features])[0]

    def predict_batch(self, feature_set: List[Song]) -> List[str]:
        """ Predicts the genres of several songs. """

        # Normalise the dataset and scale them in the same way as our training data.
        df = pd.json_normalize(asdict(song) for song in feature_set).astype(float)
        new_set = dataset.scaler.transform(df)
        new_set = Tensor(new_set).to(self.model.device)  # send to a Tensor.

        # Make predictions and return the corresponding genre.
        preds_tensor = self.model(new_set)
        preds = torch.max(preds_tensor, dim=1)

        return [genre_store[item] for item in preds.indices.tolist()]
