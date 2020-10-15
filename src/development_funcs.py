import csv

def print_select_columns(select_cols, cols, cols_inds, num_rows=5):
    """Prints a subset of the columns and rows.
    Input:
    select_cols - list of column names
    cols - dictionary: {index:column_name}
    cols_inds - dictionary: {column_name:index}
    num_rows - number of rows returned, not counting the initial row of column names"""
    with open("../input/censustract-00-10.csv", newline="") as csvfile:
        censusreader = csv.reader(csvfile, delimiter=",")
        i = 0
        for row in censusreader:
            new_row = []
            for col in select_cols:
                new_row.append(row[cols_inds[col]])
            print(new_row)
            i += 1
            if i > num_rows:
                break

def print_select_cols_and_rows(select_cols, cols, cols_inds, rowstart=1, rowend=10):
    """REVISE THIS -- THE INDEXING IS BAD
    Prints a subset of the columns and rows.
    Input:
    select_cols - list of column names
    cols - dictionary: {index:column_name}
    cols_inds - dictionary: {column_name:index}
    num_rows - number of rows returned, not counting the initial row of column names"""
    with open("../input/censustract-00-10.csv", newline="") as csvfile:
        censusreader = csv.reader(csvfile, delimiter=",")
        i = 1
        row = next(censusreader)
        for i in range(rowstart - 1):
            next(censusreader)
            i += 1
        for row in censusreader:
            new_row = []
            for col in select_cols:
                new_row.append(row[cols_inds[col]])
            print(new_row)
            i += 1
            if i > rowend:
                break

def print_select_cols_from_rows_with_X(select_cols, cols, cols_inds):
    """
    Prints a subset of the columns from rows with (X) in ppchg.
    Input:
    select_cols - list of column names
    cols - dictionary: {index:column_name}
    cols_inds - dictionary: {column_name:index}
    """
    with open("../input/censustract-00-10.csv", newline="") as csvfile:
        censusreader = csv.reader(csvfile, delimiter=",")
        with open("./logfile_X.csv", "w+", newline="") as logfile:
            logwriter = csv.writer(logfile, delimiter=",")
            i = 1
            row = next(censusreader)
            new_row = []
            for col in select_cols:
                new_row.append(row[cols_inds[col]])
            logwriter.writerow(new_row)
            for row in censusreader:
                if row[cols_inds["PPCHG"]] == '(X)':
                    new_row = []
                    for col in select_cols:
                        new_row.append(row[cols_inds[col]])
                    if row[cols_inds['POP00']] != '0':
                        new_row.append('WARNING')
                    # print(new_row)
                    logwriter.writerow(new_row)
                i += 1

def write_col_keys(cols):
    """Write the columns keys and their indices to file.
    Input: cols - dictionary: {index:column_name}
    Output: csv file with each item of dictionary on its own line.
    """
    with open("column_key.csv", "w+", newline="") as csvfile:
        column_key_writer = csv.writer(csvfile, delimiter=",")
        for i, col in cols.items():
            column_key_writer.writerow([i, col])

def write_error_rows(path_to_errors_csv, error_rows):
    """Write the row indices of rows with errors.
    Input: list of row indices with errors
    Output: csv file with each item of dictionary on its own line.
    """
    with open("row_errors.csv", "w+", newline="") as csvfile:
        row_error_writer = csv.writer(csvfile, delimiter=",")
        for ind in error_rows:
            row_error_writer.writerow([ind])

