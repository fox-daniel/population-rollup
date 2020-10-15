import csv
import population_funcs


path_to_csv = "../input/censustract-00-10.csv"
path_to_error_log = "./error_log.csv"
path_to_test_1 = "../insight_testsuite/tests/test_1/input/censustract-00-10.csv"
path_to_report = "../output/report.csv"

# dictionaries {column_index, column_name} & {column_name, column_index}
cols, cols_inds = population_funcs.create_column_dicts(path_to_csv)

select_cols = ["GEOID", "CBSA09", "CBSA_T", "POP00", "POP10", "PPCHG"]


# population_funcs.print_select_columns(select_cols, cols, cols_inds)

# num_rows = population_funcs.count_rows()
# print(num_rows)

# population_funcs.write_col_keys(cols)

# population_funcs.print_select_cols_and_rows(select_cols, cols, cols_inds, 51, 500)

# population_funcs.print_select_cols_from_rows_with_X(select_cols, cols, cols_inds)


(
    cbsa_title,
    tract_count,
    pop00_count,
    pop10_count,
    ppchg_avg,
    error_rows,
) = population_funcs.groupby_cbsa(
    path_to_csv, path_to_error_log, select_cols, cols, cols_inds, num_rows=75000
)


population_funcs.write_report(
    path_to_report,
    cols,
    cols_inds,
    cbsa_title,
    tract_count,
    pop00_count,
    pop10_count,
    ppchg_avg,
)

# print(cbsa_title.items())
# print(tract_count.items())
# print(pop00_count.items())
# print(pop10_count.items())
# print(ppchg_avg.items())
# print(len(error_rows))
# print(error_rows[:10])


# path_to_errors_csv = './row_errors.csv'
# population_funcs.write_error_rows(path_to_errors_csv, error_rows)

# [43, 108, 868, 1325, 1460, 1472, 1475, 1476, 1477, 1480]
