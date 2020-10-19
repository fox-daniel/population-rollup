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
    """Test the type of each value of each row."""
    # dictionaries {column_index, column_name} & {column_name, column_index}
    col_types = [int, int, int, int, float, float, int, int, str, any, int, str, int, int, int, int, int, float, int, float]
    cols, cols_inds = transformation.create_column_dicts(path_to_raw)
    validation.test_types(path_to_raw, path_to_log, cols_inds, col_types)


if __name__ == "__main__":
    main()
