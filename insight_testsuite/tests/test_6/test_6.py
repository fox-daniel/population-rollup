import csv
import sys
import os
sys.path.append("./ src/")
import importlib
print(os.system('pwd'))
import development
import validation
import transformation

importlib.reload(validation)
importlib.reload(transformation)
importlib.reload(development)

# file paths
path_to_raw = "./input/censustract-00-10.csv"
path_to_log_validate_0 = "./log_validate_0.csv"
path_to_log_validate_1 = "./log_validate_1.csv"
path_to_log_transform_1 = "./log_transform_1.csv"
path_to_log_transform_2 = "./log_transform_2.csv"
path_to_filled = "./output/filled.csv"
path_to_selected_columns = "./output/selected_columns.csv"
path_to_cleaned_types = "./output/cleaned_types.csv"

# dictionaries {column_index, column_name} & {column_name, column_index}
cols, cols_inds = transformation.create_column_dicts(path_to_raw)

selected_columns = ["GEOID", "CBSA09", "CBSA_T", "POP00", "POP10", "PPCHG"]
col_types = ["int", "int", "str", "int", "int", "float"]


validation.test_geoid_concat(path_to_raw, path_to_log_validate_0, cols, cols_inds)
validation.test_row_length(path_to_raw, path_to_log_validate_0)

# transform 1
transformation.fill_missing_cbsa(
    path_to_raw, path_to_filled, path_to_log_transform_1, cols_inds
)
transformation.select_columns(
    path_to_filled, path_to_selected_columns, selected_columns, cols, cols_inds
)

# dictionaries {column_index, column_name} & {column_name, column_index}
cols, cols_inds = transformation.create_column_dicts(path_to_selected_columns)

transformation.clean_types(
    path_to_selected_columns, path_to_cleaned_types, cols, cols_inds, col_types
)
(
    cbsa_title,
    tract_count,
    pop00_count,
    pop10_count,
    ppchg_avg,
    error_rows,
) = transformation.groupby_cbsa(
    path_to_cleaned_types, path_to_log_transform_2, selected_columns, cols, cols_inds
)


print(cbsa_title)
print(tract_count)
print(pop00_count)
print(pop10_count)
print(ppchg_avg)
print(error_rows)