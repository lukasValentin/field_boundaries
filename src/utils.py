
import numpy as np

from pathlib import Path


def read_npy(path: Path) -> np.ndarray:
    """
    Read a numpy array from a file.

    :param path: Path to the file.
    :return: The numpy array.
    """
    return np.load(path, allow_pickle=True)
