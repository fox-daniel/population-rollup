import csv
import sys

sys.path.append("./../../../src/")
import importlib
import validation
import transformation

importlib.reload(validation)
importlib.reload(transformation)

path_to_raw = "./input/test_input.csv"
path_to_log = "./test_log.csv"


def main():
    """Test that the GEOID is the concatenation of its components."""
    # dictionaries {column_index, column_name} & {column_name, column_index}
    cols, cols_inds = transformation.create_column_dicts(path_to_raw)
    validation.test_geoid_concat(path_to_raw, path_to_log, cols_inds)


if __name__ == "__main__":
    main()
