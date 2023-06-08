import pandas as pd

from torch.utils.data import Dataset, DataLoader, random_split
from torchvision import transforms

from sklearn.preprocessing import MinMaxScaler

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
        "index"
    ]
    """ A list of features to be ignored by the Dataset. """

    def __init__(self, csv_file, transform=None, target_transform=None):
        file = pd.read_csv(csv_file)
        file.explicit = file.explicit.replace({True: 1, False: 0})  # replace boolean values with integers.
        desired_features = set(file.columns) - set(self.ignored_features)  # remove ignored features.

        self.song_labels = file["track_genre"]
        self.song_features = file.loc[:, list(desired_features)]

        # Scale each column to be within the range [0, 1].
        self.song_features = pd.DataFrame(MinMaxScaler().fit_transform(self.song_features),
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


dataset = SpotifyTracksDataset(csv_file="data/dataset.csv",
                               transform=DataFrameToTensor(),
                               target_transform=transforms.Compose([ToLowerCase(), ToNumericGenre()]))

# Split into training and testing data along the ratio 2:1.
train_set, test_set = random_split(dataset, [76000, 38000])

train_dataloader = DataLoader(train_set, batch_size=760, shuffle=True)
test_dataloader = DataLoader(test_set, batch_size=380, shuffle=False)
