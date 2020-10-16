import csv
import sys

sys.path.append("./../../../src/")
import importlib
import development
import validation
import transformation

importlib.reload(validation)
importlib.reload(transformation)
importlib.reload(development)

path_to_raw = "./input/test_3_input.csv"
path_to_log = "./log_test_3.csv"
path_to_report = "./output/report.csv"


def main():
    """Test that the GEOID is the concatenation of its components."""
    # dictionaries {column_index, column_name} & {column_name, column_index}
    cols, cols_inds = transformation.create_column_dicts(path_to_raw)
    select_cols = ["GEOID", "CBSA09", "CBSA_T", "POP00", "POP10", "PPCHG"]
    validation.test_row_length(path_to_raw, path_to_log)


if __name__ == "__main__":
    main()
