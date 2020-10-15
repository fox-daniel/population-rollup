import csv
import sys
sys.path.append("./../../../src/")
import pipeline_funcs


def main():
	"""Test that the GEOID is the concatenation of its components."""
	

	path_to_csv = './../../../input/censustract-00-10.csv'
	# dictionaries: {column_index, column_name} and {column_name, column_index}
	cols, cols_inds = pipeline_funcs.create_column_dicts(path_to_csv)

	test_code_concat(path_to_csv, cols, cols_inds)


# def test_code_concat(path_to_csv, cols, cols_inds):
# 	cols_concat = ['GEOID', 'ST10', 'COU10', 'TRACT10', 'CBSA09', 'CBSA_T', 'POP00']

# 	with open(path_to_csv, newline = '') as csvfile:
# 		censusreader = csv.reader(csvfile, delimiter = ',')
# 		i = 0
# 		# move to the first row with data
# 		row = next(censusreader)
# 		for row in censusreader:
# 			new_row = [row[cols_inds['GEOID']],\
# 			row[cols_inds['ST10']]+row[cols_inds['COU10']]+row[cols_inds['TRACT10']]]
# 			if new_row[0] != new_row[1]:
# 				print(False)
# 			i += 1
# 		print('final row checked: ',i)

if __name__ == "__main__":
	main()

