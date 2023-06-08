from pandas import DataFrame
from torch import Tensor, from_numpy

from model.Device import get_device


class DataFrameToTensor(object):
    """ Converts a pandas `DataFrame` to a pytorch `Tensor`. """

    device = get_device()
    """ The device to send the `Tensor` to. """

    def __call__(self, df: DataFrame) -> Tensor:
        return from_numpy(df.values).float().to(self.device)
