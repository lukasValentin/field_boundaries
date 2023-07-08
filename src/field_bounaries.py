
from pathlib import Path

from utils import read_npy


def main(data_dir: Path):
    """
    Main function of the script.

    :param data_dir: Path to the data directory.
    """

    # read the numpy arrays with GLAI values
    data_dict = {}
    for glai_path in data_dir.glob('*.npy'):
        arr = read_npy(glai_path)



if __name__ == '__main__':

    data_dir = Path('data')
    main(data_dir)