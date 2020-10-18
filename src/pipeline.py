import argparse
import transformation

parser = argparse.ArgumentParser("Accept input and output file paths.")
parser.add_argument(
    "path_to_input_file",
    help="The input path should be './input/censustract-00-10.csv'.",
    type=str,
)
parser.add_argument(
    "path_to_output_file",
    help="The output path should be './output/report.csv'.",
    type=str,
)
args = parser.parse_args()

# file paths
path_to_raw = args.path_to_input_file
path_to_report = args.path_to_output_file
path_to_selected_columns = "./src/transformed_data/selected_columns.csv"
path_to_cleaned_types = "./src/transformed_data/cleaned_types.csv"
path_to_log = "./src/logs/log.csv"


# dictionaries {column_index, column_name} & {column_name, column_index}
cols, cols_inds = transformation.create_column_dicts(path_to_raw)

selected_columns = ["GEOID", "CBSA09", "CBSA_T", "POP00", "POP10", "PPCHG"]
col_types = ["int", "int", "str", "int", "int", "float"]

# transform 1
transformation.select_columns(
    path_to_raw, path_to_selected_columns, selected_columns, cols_inds
)

# new dictionaries for selected columns {column_index, column_name} & {column_name, column_index}
cols, cols_inds = transformation.create_column_dicts(path_to_selected_columns)

transformation.clean_types(path_to_selected_columns, path_to_cleaned_types, col_types)

# transform 2
(
    cbsa_title,
    tract_count,
    pop00_count,
    pop10_count,
    ppchg_avg,
    error_rows,
) = transformation.groupby_cbsa(
    path_to_cleaned_types, path_to_log, selected_columns, cols_inds
)

transformation.write_report(
    path_to_report,
    cbsa_title,
    tract_count,
    pop00_count,
    pop10_count,
    ppchg_avg,
)
