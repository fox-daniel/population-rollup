import csv
import sys

sys.path.append("./../../../src/")
import importlib
import validation
import transformation

importlib.reload(validation)
importlib.reload(transformation)

path_to_raw = "./input/censustract-00-10.csv"
path_to_log = "./test_log.csv"


def main():
    """Test how pipeline.py scales with file size in terms of time and memory use."""
    pass


if __name__ == "__main__":
    main()
