from os.path import dirname, realpath

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from torch.utils.data import Dataset, DataLoader, random_split
from torchvision import transforms

from model.transforms.DataFrameToTensor import DataFrameToTensor
from model.transforms.ToLowerCase import ToLowerCase
from model.transforms.ToNumericGenre import ToNumericGenre


class SpotifyTracksDataset(Dataset):
    """ A Dataset representation of the Spotify tracks dataset. """

    ignored_features = [
        "track_id",
        "artists",
        "album_name",
        "track_name",
        "track_genre",
        "index",
        "Unnamed: 0"
    ]
    """ A list of features to be ignored by the Dataset. """

    scaler = MinMaxScaler()
    """ An instance of the `MinMaxScaler`. """

    def __init__(self, csv_file, transform=None, target_transform=None):
        file = pd.read_csv(csv_file)
        file.explicit = file.explicit.replace({True: 1, False: 0})  # replace boolean values with integers.
        desired_features = set(file.columns) - set(self.ignored_features)  # remove ignored features.

        self.song_labels = file["track_genre"]
        self.song_features = file.loc[:, list(desired_features)]

        # Alphabetically sort the columns, so they're in the same order every time.
        self.song_features = self.song_features[sorted(self.song_features.columns)]

        # Scale each column to be within the range [0, 1].
        self.song_features = pd.DataFrame(self.scaler.fit_transform(self.song_features),
                                          columns=self.song_features.columns)

        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.song_labels)

    def __getitem__(self, idx):
        song = self.song_features.iloc[idx]
        label = self.song_labels.iloc[idx]

        if self.transform:
            song = self.transform(song)

        if self.target_transform:
            label = self.target_transform(label)

        return song, label


dataset = SpotifyTracksDataset(csv_file=f"{dirname(realpath(__file__))}/data/dataset.csv",
                               transform=DataFrameToTensor(),
                               target_transform=transforms.Compose([ToLowerCase(), ToNumericGenre()]))

# Split into training and testing data along the ratio 2:1.
train_set, test_set = random_split(dataset, [76000, 38000])

train_dataloader = DataLoader(train_set, batch_size=760, shuffle=True)
test_dataloader = DataLoader(test_set, batch_size=380, shuffle=False)

if __name__ == "__main__":
    print(
        "--- Using 🎹 Spotify Tracks Dataset: https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset "
        "--- \n")
    print(f"There are {len(dataset.song_features.columns)} columns:")

    for index, column in enumerate(dataset.song_features.columns):
        print(f" - {column}")

    print(f"\nTraining Data - size of {len(train_set)}, batch size of {train_dataloader.batch_size}")
    print(f"Test Data - size of {len(test_set)}, batch size of {test_dataloader.batch_size}")
