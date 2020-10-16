import csv
import sys

sys.path.append("./../../../src/")
import importlib
import development_funcs
import validation_funcs
import transformation_funcs

importlib.reload(validation_funcs)
importlib.reload(transformation_funcs)
importlib.reload(development_funcs)

path_to_raw = "./input/test_3_input.csv"
path_to_log = "./log_test_3.csv"
path_to_report = "./output/report.csv"


def main():
    """Test that the GEOID is the concatenation of its components."""
    # dictionaries {column_index, column_name} & {column_name, column_index}
    cols, cols_inds = transformation_funcs.create_column_dicts(path_to_raw)
    select_cols = ["GEOID", "CBSA09", "CBSA_T", "POP00", "POP10", "PPCHG"]
    validation_funcs.test_row_length(path_to_raw, path_to_log)


if __name__ == "__main__":
    main()
