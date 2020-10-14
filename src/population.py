import csv
from collections import defaultdict
import population_funcs


# dictionaries {column_index, column_name} & {column_name, column_index}
path_to_csv = '../input/censustract-00-10.csv'
cols, cols_inds = population_funcs.create_column_dicts(path_to_csv)

select_cols= ['GEOID', 'CBSA09', 'CBSA_T', 'POP00', 'POP10', 'PPCHG']


# population_funcs.print_select_columns(select_cols, cols, cols_inds)

# num_rows = population_funcs.count_rows()
# print(num_rows)

# population_funcs.write_col_keys(cols)	

def groupby_cbsa(path_to_csv, select_cols):
	tract_count = defaultdict(int)
	pop00_count = defaultdict(int)
	pop10_count = defaultdict(int)
	ppchg_avg = defaultdict(int)
	with open(path_to_csv, newline = '') as csvfile:
		censusreader = csv.reader(csvfile, delimiter = ',')
		row = next(censusreader)
		for row in censusreader:
			tract_count[row[cols_inds['CBSA09']]] += 1
			pop00_count[row[cols_inds['CBSA09']]] += int(row[cols_inds['POP00']])
			pop10_count[row[cols_inds['CBSA09']]] += int(row[cols_inds['POP10']])
			ppchg_avg[row[cols_inds['CBSA09']]] += float(row[cols_inds['PPCHG']])
		for k, v in ppchg_avg.items():
			ppchg_avg[k] = round(ppchg_avg[k]/tract_count[k],2)
	return dict(tract_count), dict(pop00_count), dict(pop10_count), dict(ppchg_avg) 

path_to_test_1 = '../insight_testsuite/tests/test_1/input/censustract-00-10.csv'
tract_count, pop00_count, pop10_count, ppchg_avg = groupby_cbsa(path_to_test_1, select_cols)
print(tract_count.items())
print(pop00_count.items())
print(pop10_count.items())
print(ppchg_avg.items())