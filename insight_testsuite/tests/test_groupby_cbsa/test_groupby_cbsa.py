import csv
import sys

sys.path.append("./../../../src/")
import importlib
import validation
import transformation

importlib.reload(validation)
importlib.reload(transformation)

path_to_raw = "./input/censustract-00-10.csv"
path_to_selected_columns = "./output/transformed.csv"
path_to_report = "./output/report.csv"
path_to_log = "./test_log.csv"


def main():
    """Test the type of each value of each row."""
    # dictionaries {column_index, column_name} & {column_name, column_index}
    selected_columns = ["GEOID", "CBSA09", "CBSA_T", "POP00", "POP10", "PPCHG"]
    cols, cols_inds = transformation.create_column_dicts(path_to_raw)
    transformation.select_columns(
        path_to_raw, path_to_selected_columns, selected_columns, cols_inds
    )

    cols, cols_inds = transformation.create_column_dicts(path_to_selected_columns)
    (
        cbsa_title,
        tract_count,
        pop00_count,
        pop10_count,
        ppchg_avg,
        error_rows,
    ) = transformation.groupby_cbsa(
        path_to_selected_columns, path_to_log, selected_columns, cols_inds
    )

    transformation.write_report(
        path_to_report,
        cbsa_title,
        tract_count,
        pop00_count,
        pop10_count,
        ppchg_avg,
    )


if __name__ == "__main__":
    main()
