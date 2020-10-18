import csv
from datetime import datetime


def test_row_length(path_to_csv, path_to_log, length=None):
    """This validates that the row length stays constant. The default
    rowlength is that of the first row. It can also be specified as
    an argument.
    """
    with open(path_to_csv, newline="") as csvfile:
        censusreader = csv.reader(csvfile, delimiter=",")
        with open(path_to_log, mode="a", newline="") as logfile:
            rowlength_writer = csv.writer(logfile, delimiter=",")
            rowlength_writer.writerow(
                [
                    f"****Rows that have a different length than the first or as specified.**** \n Returned from validation.test_row_length() at {datetime.now().isoformat(timespec='seconds')} \n Rows with errors:"
                ]
            )
            i = 0
            error_found = False
            # move to the first row with data
            row = next(censusreader)
            if length is None:
                row_length = len(row)
            else:
                row_length = length
            rowlength_writer.writerow(
                [f"Rows should have {row_length} columns."]
            )
            for row in censusreader:
                if len(row) != row_length:
                    rowlength_writer.writerow(row)
                    error_found = True
                i += 1
            if error_found == False:
                rowlength_writer.writerow(["No errors found:)"])
            rowlength_writer.writerow(["final row checked: {0}.".format(i)])
            rowlength_writer.writerow([])
            rowlength_writer.writerow([])

def test_types(path_to_input, path_to_log, col_types):
    """Test if values conform to type requirements.
    Column Names: GEOID,ST10,COU10,TRACT10,AREAL10,AREAW10,CSA09,CBSA09,CBSA_T,MDIV09,CSI,COFLG,POP00,HU00,POP10,HU10,NPCHG,PPCHG,NHCHG,PHCHG
    Column Types: int, int, int, int, float, float, int, int, str, any, int, str, int, int, int, int, int, float, int, float
    """

    with open(path_to_input, newline="") as inputfile:
        inputreader = csv.reader(inputfile, delimiter=",")
        with open(path_to_log, mode="a", newline="") as logfile:
            logwriter = csv.writer(logfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)
            logwriter.writerow(
                [
                    f"****Rows for which values do not conform to data type.**** \n Returned from validation.test_types() at {datetime.now().isoformat(timespec='seconds')} \n Row with errors followed by a row with problem values:"
                ]
            )
            row = next(inputreader)
            for row in inputreader:
                errors_in_row = {}
                error = False
                for i, atype in enumerate(col_types):
                    try:
                        row[i] = clean_type(row[i], atype)
                    except TypeError as err:
                        error = True
                        errors_in_row[i] = (err, row[i])
                if error == True
                transwriter.writerow(row)
                transwriter.writerow([error for error in errors_in_row])

def test_geoid_concat(path_to_csv, path_to_log, cols_inds):
    """This tests whether GEOID is the concatenation of ST10, COU1, TRACT10."""
    cols_concat = ["GEOID", "ST10", "COU10", "TRACT10"]

    with open(path_to_csv, newline="") as csvfile:
        censusreader = csv.reader(csvfile, delimiter=",")
        with open(path_to_log, mode="a", newline="") as logfile:
            logwriter = csv.writer(logfile, delimiter=",", quoting=csv.QUOTE_MINIMAL)
            logwriter.writerow(
                [
                    f"****Rows for which GEOID is not the concatenation of its parts.**** \n Returned from validation.test_geoid_concat() at {datetime.now().isoformat(timespec='seconds')} \n Rows with errors:"
                ]
            )
            rows_checked = 0
            rows_with_errors = 0
            error_found = False
            # move to the first row with data
            row = next(censusreader)
            for row in censusreader:
                if row[cols_inds["GEOID"]] != str(row[cols_inds["ST10"]]) + str(
                    row[cols_inds["COU10"]]
                ) + str(row[cols_inds["TRACT10"]]):
                    error_found = True
                    logwriter.writerow(row)
                    rows_with_errors += 1
                rows_checked += 1
            if error_found == False:
                logwriter.writerow(["****No errors found.****)"])
            else:
                logwriter.writerow([f"{rows_with_errors} row(s) with errors."])
            logwriter.writerow(["Rows checked: {0}.".format(rows_checked)])
            logwriter.writerow([])
            logwriter.writerow([])

def count_rows(path_to_csv):
    with open(path_to_csv, newline="") as csvfile:
        censusreader = csv.reader(csvfile, delimiter=",")
        i = 0
        for row in censusreader:
            i += 1
        return i
