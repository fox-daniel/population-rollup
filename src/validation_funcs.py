import csv

def test_geoid_concat(path_to_csv, path_to_log, cols, cols_inds):
	"""This tests whether GEOID is the concatenation of ST10+COU1-+TRACT10."""
	cols_concat = ['GEOID', 'ST10', 'COU10', 'TRACT10', 'CBSA09', 'CBSA_T', 'POP00']

	with open(path_to_csv, newline = '') as csvfile:
		censusreader = csv.reader(csvfile, delimiter = ',')
		with open(path_to_log, mode = "a", newline = "") as logfile:
			geowriter = csv.writer(logfile, delimiter=",")
			geowriter.writerow(['Rows for which GEOID is not the concatenation of its parts.'])
			i = 0
			error_found = False
			# move to the first row with data
			row = next(censusreader)
			for row in censusreader:
				new_row = [row[cols_inds['GEOID']],\
				row[cols_inds['ST10']]+row[cols_inds['COU10']]+row[cols_inds['TRACT10']]]
				if new_row[0] != new_row[1]:
					error_found = True
					geowriter.writerow(row)
				i += 1
			if error_found == False:
				geowriter.writerow(['No errors found:)'])	
			geowriter.writerow(['final row checked: {0}'.format(i)])

def count_rows(path_to_csv):
    with open(path_to_csv, newline="") as csvfile:
        censusreader = csv.reader(csvfile, delimiter=",")
        i = 0
        for row in censusreader:
            i += 1
        return i


def test_row_length(path_to_csv, path_to_log, length = None):
	
	with open(path_to_csv, newline = '') as csvfile:
		censusreader = csv.reader(csvfile, delimiter = ',')
		with open(path_to_log, mode = "a", newline = "") as logfile:
			rowlength_writer = csv.writer(logfile, delimiter=",")
			rowlength_writer.writerow(['Rows that have a different length than the first or as specified.'])
			i = 0
			error_found = False
			# move to the first row with data
			row = next(censusreader)
			if length is None:
				row_length = len(row)
			else:
				row_length = length
			for row in censusreader:
				if len(row) != row_length:
					rowlength_writer.writerow(row)
					error_found = True
				i += 1
			if error_found == False:
				rowlength_writer.writerow(['No errors found:)'])
			rowlength_writer.writerow(['final row checked: {0}'.format(i)])