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

def count_tracts(path_to_csv, select_cols):
	tract_count = defaultdict(int)
	with open(path_to_csv, newline = '') as csvfile:
		censusreader = csv.reader(csvfile, delimiter = ',')
		row = next(censusreader)
		for row in censusreader:
			tract_count[row[cols_inds['CBSA09']]] +=1	
	return dict(tract_count)

path_to_test_1 = '../insight_testsuite/tests/test_1/input/censustract-00-10.csv'
tract_count = count_tracts(path_to_test_1, select_cols)
print(tract_count.items())
print(tract_count['28540'])