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
tract_count, pop00_count, pop10_count, ppchg_avg = population_funcs.groupby_cbsa(path_to_test_1, select_cols, cols, cols_inds)
print(tract_count.items())
print(pop00_count.items())
print(pop10_count.items())
print(ppchg_avg.items())

path_to_report = 'report.csv'
def write_report(path_to_report, cols, cols_inds, tract_count, pop00_count, pop10_count, ppchg_avg):
	with open(path_to_report, 'w', newline = '') as csvfile:
		csvwriter = csv.writer(csvfile, delimiter = ',')
		for k in tract_count.keys():
			print(k, pop00_count[k], pop10_count[k], ppchg_avg[k])
			csvwriter.writerow([k, tract_count[k], pop00_count[k], pop10_count[k], ppchg_avg[k]])

write_report(path_to_report, cols, cols_inds, tract_count, pop00_count, pop10_count, ppchg_avg)