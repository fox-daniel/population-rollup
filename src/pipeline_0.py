import csv
import importlib
import development_funcs
import validation_funcs
import transformation_funcs

importlib.reload(validation_funcs)
importlib.reload(transformation_funcs)
importlib.reload(development_funcs)

# file paths
path_to_raw = "../input/censustract-00-10.csv"

path_to_log_validate_0 = "./log_validate_0.csv"
path_to_log_validate_1 = "./log_validate_1.csv"
path_to_log_validate_2 = "./log_validate_2.csv"

path_to_filled = "./transformed_data/filled.csv"
path_to_log_filled = "./logs/log_filled.csv"
path_to_selected_columns = "./transformed_data/selected_columns.csv"
path_to_cleaned_types = "./transformed_data/cleaned_types.csv"
path_to_log_groupby = "./logs/log_groupby.csv"
path_to_test_1 = "../insight_testsuite/tests/test_1/input/censustract-00-10.csv"

path_to_report = "../output/report.csv"

# dictionaries {column_index, column_name} & {column_name, column_index}
cols, cols_inds = transformation_funcs.create_column_dicts(path_to_raw)

selected_columns = ["GEOID", "CBSA09", "CBSA_T", "POP00", "POP10", "PPCHG"]
col_types = ["int", "int", "str", "int", "int", "float"]

# validation 0
validation_funcs.test_geoid_concat(path_to_raw, path_to_log_validate_0, cols, cols_inds)
validation_funcs.test_row_length(path_to_raw, path_to_log_validate_0)

# transform 1
transformation_funcs.fill_missing_cbsa(
    path_to_raw, path_to_filled, path_to_log_filled, cols_inds
)
transformation_funcs.select_columns(
    path_to_filled, path_to_selected_columns, selected_columns, cols, cols_inds
)

# dictionaries {column_index, column_name} & {column_name, column_index}
cols, cols_inds = transformation_funcs.create_column_dicts(path_to_selected_columns)


transformation_funcs.clean_types(
    path_to_selected_columns, path_to_cleaned_types, cols, cols_inds, col_types
)
(
    cbsa_title,
    tract_count,
    pop00_count,
    pop10_count,
    ppchg_avg,
    error_rows,
) = transformation_funcs.groupby_cbsa(
    path_to_cleaned_types, path_to_log_groupby, selected_columns, cols, cols_inds
)

# print(cbsa_title['46900'])
# print(tract_count['46900'])
# print(pop00_count['46900'])
# print(pop10_count['46900'])
# print(ppchg_avg['46900'])

