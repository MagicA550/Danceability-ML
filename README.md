# Danceability-ML

Many people, myself included, find that different songs elicit
memories of a specific time in their life, such as a family holiday,
spending time with close friends, or what projects you were
working on. Danceability is a work-in-progress project enabling users to
generate Spotify song recommendations based on a time period in
their listening history.

This repository contains a Neural Network written in PyTorch to recognise
genres by song features and will interact with Spotify's API to generate
necessary recommendations. Future layers built on this back-end will include
interfaces to interact with the network, such as for the web or via a
Discord Bot.

## Usage

Although I wouldn't advise it, as it isn't complete, below are steps to use
the PyTorch Model within:

1. Download the [Spotify Tracks Dataset](https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset)
   on Kaggle and place in `/model/data`.
2. Execute `/model/SpotifyTracksDataset.py` to check that it has been
   initialised correctly.
3. Execute `/model/Model.py` to train the Neural Network (tune parameters
   here if you see fit). This will save the network in `/model/data/model.pth`.
4. Execute `/main.py` to start the Flask API to interact with the model.

## Todos

- Improve model accuracy
- Add integration with Spotify
