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

# file paths
path_to_raw = "./input/censustract-00-10.csv"
path_to_log_validate_0 = "./log_validate_0.csv"
path_to_log_validate_1 = "./log_validate_1.csv"
path_to_log_transform_1 = "./log_transform_1.csv"
path_to_filled = "./output/filled.csv"
path_to_selected_cols = "./output/selected_columns.csv"


# dictionaries {column_index, column_name} & {column_name, column_index}
cols, cols_inds = transformation_funcs.create_column_dicts(path_to_raw)

selected_columns = ["GEOID", "CBSA09", "CBSA_T", "POP00", "POP10", "PPCHG"]


validation_funcs.test_geoid_concat(path_to_raw, path_to_log_validate_0, cols, cols_inds)
validation_funcs.test_row_length(path_to_raw, path_to_log_validate_0)
transformation_funcs.fill_missing_cbsa(path_to_raw, path_to_filled, path_to_log_transform_1, cols_inds)
transformation_funcs.select_columns(path_to_filled, path_to_selected_cols, selected_columns, cols, cols_inds)