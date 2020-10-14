import csv


def create_column_dict():
	cols = {}
	with open('../input/censustract-00-10.csv', newline = '') as csvfile:
		censusreader = csv.reader(csvfile, delimiter = ',')
		row = next(censusreader)
		for i, col in enumerate(row):
			cols[i] = col
	return cols

# dictionary {column_index, column_name}
cols = create_column_dict()
# dictionary {column_name, column_index}
cols_inds = {v:k for k, v in cols.items()}


cols_used = ['GEOID', 'ST10', 'COU10', 'TRACT10', 'CBSA09', 'CBSA_T', 'POP00', 'POP10', 'PPCHG']

def print_select_columns():
	with open('../input/censustract-00-10.csv', newline = '') as csvfile:
		censusreader = csv.reader(csvfile, delimiter = ',')
		i = 0
		for row in censusreader:
			new_row = []
			for col in cols_used:
				new_row.append(row[cols_inds[col]])
			print(new_row)
			i += 1
			if i > 5:
				break

# print_select_columns()

def count_rows():
	with open('../input/censustract-00-10.csv', newline = '') as csvfile:
		censusreader = csv.reader(csvfile, delimiter = ',')
		i = 0
		for row in censusreader:
			i += 1
		return i

# num_rows = count_rows()
# print(num_rows)

def test_code_concat():
	cols_concat = ['GEOID', 'ST10', 'COU10', 'TRACT10', 'CBSA09', 'CBSA_T', 'POP00']

	with open('../input/censustract-00-10.csv', newline = '') as csvfile:
		censusreader = csv.reader(csvfile, delimiter = ',')
		i = 0
		# move to the first row with data
		row = next(censusreader)
		for row in censusreader:
			new_row = [row[cols_inds['GEOID']],\
			row[cols_inds['ST10']]+row[cols_inds['COU10']]+row[cols_inds['TRACT10']]]
			if new_row[0] != new_row[1]:
				print(False)
			i += 1
		print('final row checked: ',i)
			# if i >= n:
			# 	print('final row checked: ',i)
			# 	break

test_code_concat()

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


