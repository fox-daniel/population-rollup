import csv
import importlib
import os
import argparse
import development
import validation
import transformation

importlib.reload(validation)
importlib.reload(transformation)
importlib.reload(development)

parser=argparse.ArgumentParser("Accept input and output file paths.")
parser.add_argument("path_to_input_file", help="The input path should be './input/censustract-00-10.csv'.", type=str)
parser.add_argument("path_to_output_file", help="The output path should be './output/report.csv'.", type=str)
args = parser.parse_args()

print("From within pipeline.py, os.system('pwd'):")
print(os.system("pwd"))

# file paths
path_to_raw = args.path_to_input_file
path_to_report = args.path_to_output_file

path_to_log_validate_0 = "./src/logs/log_validate_0.csv"
path_to_log_validate_1 = "./src/logs/log_validate_1.csv"
path_to_log_validate_2 = "./src/logs/log_validate_2.csv"

path_to_filled = "./src/transformed_data/filled.csv"
path_to_log_filled = "./src/logs/log_filled.csv"
path_to_selected_columns = "./src/transformed_data/selected_columns.csv"
path_to_cleaned_types = "./src/transformed_data/cleaned_types.csv"
path_to_log_groupby = "./src/logs/log_groupby.csv"

path_to_test_1 = "./insight_testsuite/tests/test_1/input/censustract-00-10.csv"



# dictionaries {column_index, column_name} & {column_name, column_index}
cols, cols_inds = transformation.create_column_dicts(path_to_raw)

selected_columns = ["GEOID", "CBSA09", "CBSA_T", "POP00", "POP10", "PPCHG"]
col_types = ["int", "int", "str", "int", "int", "float"]

# validation 0
validation.test_geoid_concat(path_to_raw, path_to_log_validate_0, cols, cols_inds)
validation.test_row_length(path_to_raw, path_to_log_validate_0)

# transform 1
transformation.select_columns(
    path_to_raw, path_to_selected_columns, selected_columns, cols, cols_inds
)

# new dictionaries for selected columns {column_index, column_name} & {column_name, column_index}
cols, cols_inds = transformation.create_column_dicts(path_to_selected_columns)

transformation.clean_types(
    path_to_selected_columns, path_to_cleaned_types, cols, cols_inds, col_types
)

# transform 2
(
    cbsa_title,
    tract_count,
    pop00_count,
    pop10_count,
    ppchg_avg,
    error_rows,
) = transformation.groupby_cbsa(
    path_to_cleaned_types, path_to_log_groupby, selected_columns, cols, cols_inds
)

transformation.write_report(
    path_to_report,
    cols,
    cols_inds,
    cbsa_title,
    tract_count,
    pop00_count,
    pop10_count,
    ppchg_avg,
)
