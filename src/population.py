import csv

import population_funcs


# dictionaries {column_index, column_name} & {column_name, column_index}
path_to_csv = '../input/censustract-00-10.csv'
cols, cols_inds = population_funcs.create_column_dicts(path_to_csv)

select_cols= ['GEOID', 'CBSA09', 'CBSA_T', 'POP00', 'POP10', 'PPCHG']


# population_funcs.print_select_columns(select_cols, cols, cols_inds)

# num_rows = population_funcs.count_rows()
# print(num_rows)

# population_funcs.write_col_keys(cols)	


path_to_test_1 = '../insight_testsuite/tests/test_1/input/censustract-00-10.csv'
cbsa_title, tract_count, pop00_count, pop10_count, ppchg_avg = population_funcs.groupby_cbsa(path_to_test_1, select_cols, cols, cols_inds)
print(cbsa_title.items())
print(tract_count.items())
print(pop00_count.items())
print(pop10_count.items())
print(ppchg_avg.items())

path_to_report = 'report.csv'
population_funcs.write_report(path_to_report, cols, cols_inds, cbsa_title, tract_count, pop00_count, pop10_count, ppchg_avg)