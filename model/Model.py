import torch
from torch import nn
from torch import optim
from torch.utils.data import DataLoader

from model.Device import get_device
from model.SpotifyTracksDataset import train_dataloader, test_dataloader


class Model(nn.Module):
    """ A pytorch module containing the network. """

    def __init__(self):
        super(Model, self).__init__()
        self.flatten = nn.Flatten()

        self.linear_tanh_stack = nn.Sequential(
            nn.Linear(15, 64),
            nn.Tanh(),
            nn.Linear(64, 128),
            nn.Tanh(),
            nn.Linear(128, 256),
            nn.Tanh(),
            nn.Linear(256, 144)
        )

        self.to(get_device())

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_tanh_stack(x)
        return logits


def train_loop(dataloader: DataLoader, model: nn.Module, loss_fn: nn.CrossEntropyLoss, optimizer: optim.Adam):
    """ Completes an epoch of training on the model using the given DataLoader, loss function and optimizer. """

    size = len(dataloader.dataset)
    model.train()

    for batch, (X, y) in enumerate(dataloader):
        X = X.to(get_device())
        y = y.to(get_device())
        pred = model(X)
        loss = loss_fn(pred, y)

        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        if batch % 100 == 0:
            loss, current = loss.item(), (epoch + 1) * len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")


def test_loop(dataloader: DataLoader, model: nn.Module, loss_fn: nn.CrossEntropyLoss):
    """ Completes a testing epoch on the model using the given DataLoader and loss function. """

    model.eval()
    total_loss, total_correct, total_samples = 0.0, 0, 0

    with torch.no_grad():
        for X, y in dataloader:
            X = X.to(get_device())
            y = y.to(get_device())
            outputs = model(X)
            loss = loss_fn(outputs, y)

            _, predicted = torch.max(outputs, dim=1)
            total_loss += loss.item() * X.size(0)
            total_correct += torch.sum(predicted == y).item()
            total_samples += y.size(0)

        avg_loss = total_loss / total_samples
        accuracy = total_correct / total_samples
        print(f"Test Error: \n Accuracy: {accuracy}, Avg loss: {avg_loss} \n")


if __name__ == "__main__":
    # If executed standalone, train and save the model.
    num_epochs = 100

    model = Model()
    loss_fn = nn.CrossEntropyLoss().to(get_device())
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    for epoch in range(num_epochs):
        print(f"Epoch {epoch + 1}")
        train_loop(train_dataloader, model, loss_fn, optimizer)
        test_loop(test_dataloader, model, loss_fn)

    torch.save(model.state_dict(), "data/model.pth")
