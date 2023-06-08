from torch import cuda, device


def get_device() -> device:
    """ Returns the appropriate device for pytorch-based objects to be sent to. """

    if cuda.is_available():
        return device("cuda:0")

    return device("cpu")
