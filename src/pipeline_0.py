import csv
import importlib
import development_funcs
import validation_funcs
import transformation_funcs

importlib.reload(validation_funcs)
importlib.reload(transformation_funcs)
importlib.reload(development_funcs)

path_to_raw = "../input/censustract-00-10.csv"
path_to_log_validate_0 = "./log_validate_0.csv"
path_to_log_validate_1 = "./log_validate_1.csv"
path_to_log_validate_2 = "./log_validate_2.csv"
path_to_test_1 = "../insight_testsuite/tests/test_1/input/censustract-00-10.csv"
path_to_report = "../output/report.csv"

# dictionaries {column_index, column_name} & {column_name, column_index}
cols, cols_inds = transformation_funcs.create_column_dicts(path_to_raw)

select_cols = ["GEOID", "CBSA09", "CBSA_T", "POP00", "POP10", "PPCHG"]


validation_funcs.test_geoid_concat(path_to_raw, path_to_log_validate_0, cols, cols_inds)

validation_funcs.test_row_length(path_to_raw, path_to_log_validate_0)

