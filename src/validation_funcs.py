import csv

def test_code_concat(path_to_csv, cols, cols_inds):
	cols_concat = ['GEOID', 'ST10', 'COU10', 'TRACT10', 'CBSA09', 'CBSA_T', 'POP00']

	with open(path_to_csv, newline = '') as csvfile:
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

def count_rows(path_to_csv):
    with open(path_to_csv, newline="") as csvfile:
        censusreader = csv.reader(csvfile, delimiter=",")
        i = 0
        for row in censusreader:
            i += 1
        return i

def write_error_rows(path_to_errors_csv, error_rows):
    """Write the row indices of rows with errors.
    Input: list of row indices with errors
    Output: csv file with each item of dictionary on its own line.
    """
    with open("row_errors.csv", "w+", newline="") as csvfile:
        row_error_writer = csv.writer(csvfile, delimiter=",")
        for ind in error_rows:
            row_error_writer.writerow([ind])