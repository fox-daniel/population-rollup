import csv

def create_column_dict():
	cols = {}
	with open('../input/censustract-00-10.csv', newline = '') as csvfile:
		censusreader = csv.reader(csvfile, delimiter = ',')
		row = next(censusreader)
		for i, col in enumerate(row):
			cols[i] = col
	return cols

cols = create_column_dict()
cols_inds = {v:k for k, v in cols.items()}

print(cols)
print(cols_inds)

cols_used = ['GEOID', 'ST10', 'COU10', 'TRACT10', 'POP00', 'HU00', 'POP10', 'HU10', 'PPCHG']

# def print_select_columns():
# 	with open('../input/censustract-00-10.csv', newline = '') as csvfile:
# 		censusreader = csv.reader(csvfile, delimiter = ',')
# 		i = 0
# 		for row in censusreader:
# 			for col in cols_used:
# 				print(row[])
# 			i += 1
# 			if i > 5:
# 				break
# 	return cols


# to use within csv reader
	# i = 0
	# for row in censusreader:
	# 	print(row[:2])
	# 	i+=1
	# 	if i > 5:
	# 		break

def write_col_keys():
	"""Write the columns keys and their indices to file."""
	with open('column_key.csv', 'w', newline = '') as csvfile:
		column_key_writer = csv.writer(csvfile, delimiter = ',')
		for i, col in cols.items():
			column_key_writer.writerow([i,col])

