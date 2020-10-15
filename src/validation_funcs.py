import csv

def test_geoid_concat(path_to_csv, path_to_log, cols, cols_inds):
	cols_concat = ['GEOID', 'ST10', 'COU10', 'TRACT10', 'CBSA09', 'CBSA_T', 'POP00']

	with open(path_to_csv, newline = '') as csvfile:
		censusreader = csv.reader(csvfile, delimiter = ',')
		with open(path_to_log, mode = "w", newline = "") as logfile:
			geowriter = csv.writer(logfile, delimiter=",")
			i = 0
			# move to the first row with data
			row = next(censusreader)
			for row in censusreader:
				new_row = [row[cols_inds['GEOID']],\
				row[cols_inds['ST10']]+row[cols_inds['COU10']]+row[cols_inds['TRACT10']]]
				if new_row[0] != new_row[1]:
					geowriter.writerow(row)
				i += 1
			geowriter.writerow(['final row checked: {0}'.format(i)])

def count_rows(path_to_csv):
    with open(path_to_csv, newline="") as csvfile:
        censusreader = csv.reader(csvfile, delimiter=",")
        i = 0
        for row in censusreader:
            i += 1
        return i

