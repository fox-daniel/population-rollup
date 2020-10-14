import csv


def create_column_dicts(path_to_csv):
	"""Creates dictionaries: {column_index, column_name} and 
	{column_name, column_index}"""
	cols = {}
	with open(path_to_csv, newline = '') as csvfile:
		censusreader = csv.reader(csvfile, delimiter = ',')
		row = next(censusreader)
		for i, col in enumerate(row):
			cols[i] = col
	# dictionary {column_name, column_index}
	cols_inds = {v:k for k, v in cols.items()}
	return cols, cols_inds

def print_select_columns(select_cols, cols, cols_inds, num_rows = 5):
	"""Prints a subset of the columns and rows.
	Input: 
	select_cols: list of column names
	cols: dictionary: {index:column_name}
	cols_inds: dictionary: {column_name:index}
	num_rows: number of rows returned, not counting the initial row of column names"""
	with open('../input/censustract-00-10.csv', newline = '') as csvfile:
		censusreader = csv.reader(csvfile, delimiter = ',')
		i = 0
		for row in censusreader:
			new_row = []
			for col in select_cols:
				new_row.append(row[cols_inds[col]])
			print(new_row)
			i += 1
			if i > num_rows:
				break

def count_rows():
	with open('../input/censustract-00-10.csv', newline = '') as csvfile:
		censusreader = csv.reader(csvfile, delimiter = ',')
		i = 0
		for row in censusreader:
			i += 1
		return i
			

def write_col_keys(cols):
	"""Write the columns keys and their indices to file.
	Input: cols: dictionary: {index:column_name}
	Output: csv file with each item of dictionary on its own line.
	"""
	with open('column_key.csv', 'w', newline = '') as csvfile:
		column_key_writer = csv.writer(csvfile, delimiter = ',')
		for i, col in cols.items():
			column_key_writer.writerow([i,col])


