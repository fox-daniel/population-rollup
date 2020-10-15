import csv
import importlib
import pipeline_funcs
importlib.reload(pipeline_funcs)


path_to_raw = "../input/censustract-00-10.csv"
path_to_log_validate_0 = "./log_validate_0.csv"
path_to_log_validate_1 = "./log_validate_1.csv"
path_to_log_validate_2 = "./log_validate_2.csv"
path_to_test_1 = "../insight_testsuite/tests/test_1/input/censustract-00-10.csv"
path_to_report = "../output/report.csv"

# dictionaries {column_index, column_name} & {column_name, column_index}
cols, cols_inds = pipeline_funcs.create_column_dicts(path_to_raw)

select_cols = ["GEOID", "CBSA09", "CBSA_T", "POP00", "POP10", "PPCHG"]

