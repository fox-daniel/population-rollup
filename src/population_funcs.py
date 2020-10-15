import csv
from collections import defaultdict


def create_column_dicts(path_to_csv):
    """Creates dictionaries: {column_index, column_name} and
    {column_name, column_index}"""
    cols = {}
    with open(path_to_csv, newline="") as csvfile:
        censusreader = csv.reader(csvfile, delimiter=",")
        row = next(censusreader)
        for i, col in enumerate(row):
            cols[i] = col
    # dictionary {column_name, column_index}
    cols_inds = {v: k for k, v in cols.items()}
    return cols, cols_inds


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


def count_rows():
    with open("../input/censustract-00-10.csv", newline="") as csvfile:
        censusreader = csv.reader(csvfile, delimiter=",")
        i = 0
        for row in censusreader:
            i += 1
        return i


def write_col_keys(cols):
    """Write the columns keys and their indices to file.
    Input: cols - dictionary: {index:column_name}
    Output: csv file with each item of dictionary on its own line.
    """
    with open("column_key.csv", "w+", newline="") as csvfile:
        column_key_writer = csv.writer(csvfile, delimiter=",")
        for i, col in cols.items():
            column_key_writer.writerow([i, col])


def groupby_cbsa(path_to_csv, path_to_error_log, select_cols, cols, cols_inds, num_rows=1000):
    """
    Aggregate population data into CBSA's and return dictionaries with the CBSA09 code as the key.
    Input:
    path_to_csv -  the path to csv file with the population data
    cols - dictionary: {index:column_name}
    cols_inds - dictionary: {column_name:index}
    num_rows - the maximum number of rows to use as input
    Output:

    """
    cbsa_title = {}
    tract_count = defaultdict(int)
    pop00_count = defaultdict(int)
    pop10_count = defaultdict(int)
    ppchg_avg = defaultdict(int)
    error_rows = []
    with open(path_to_error_log, "w+", newline="") as errorfile:
        errorwriter = csv.writer(errorfile, delimiter=",")
        with open(path_to_csv, newline="") as csvfile:
            censusreader = csv.reader(csvfile, delimiter=",")
            row = next(censusreader)
            i = 0
            for row in censusreader:                
                try:
                    cbsa_title[row[cols_inds["CBSA09"]]] = row[cols_inds["CBSA_T"]]                    
                    tract_count[row[cols_inds["CBSA09"]]] += 1
                    pop00_count[row[cols_inds["CBSA09"]]] += int(
                        row[cols_inds["POP00"]]
                    )
                    pop10_count[row[cols_inds["CBSA09"]]] += int(
                        row[cols_inds["POP10"]]
                    )
                    if row[cols_inds["PPCHG"]] == '(X)':
                        ppchg_avg[row[cols_inds["CBSA09"]]] = '(X)'
                        # print('first conditional: ', ppchg_avg[row[cols_inds["CBSA09"]]])
                        # errorwriter.writerow(['ppchg is (X)']+[row[cols_inds[col]] for col in select_cols])
                    elif isinstance(row[cols_inds["PPCHG"]], str) & (ppchg_avg[row[cols_inds["CBSA09"]]] != '(X)'):
                        ppchg_avg[row[cols_inds["CBSA09"]]] += float(
                        row[cols_inds["PPCHG"]].replace(",",""))
                    elif isinstance(row[cols_inds["PPCHG"]], float) or isinstance(row[cols_inds["PPCHG"]], int):
                        ppchg_avg[row[cols_inds["CBSA09"]]] += float(
                            row[cols_inds["PPCHG"]]
                        )
                except TypeError as err:
                    errorwriter.writerow(['TypeError: ']+[row[cols_inds[col]] for col in select_cols])
                except ValueError as err:
                    errorwriter.writerow(['ValueError: ']+[row[cols_inds[col]] for col in select_cols])
                i += 1
                if i >= num_rows:
                    break
    for k, v in ppchg_avg.items():
        if ppchg_avg[k] != '(X)':
            ppchg_avg[k] = round(ppchg_avg[k] / tract_count[k], 2)
    return cbsa_title, tract_count, pop00_count, pop10_count, ppchg_avg, error_rows


def write_report(
    path_to_report,
    cols,
    cols_inds,
    cbsa_title,
    tract_count,
    pop00_count,
    pop10_count,
    ppchg_avg,
):
    with open(path_to_report, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=",")
        for k in tract_count.keys():
            # print(k, pop00_count[k], pop10_count[k], ppchg_avg[k])
            csvwriter.writerow(
                [
                    k,
                    cbsa_title[k],
                    tract_count[k],
                    pop00_count[k],
                    pop10_count[k],
                    ppchg_avg[k],
                ]
            )


def write_error_rows(path_to_errors_csv, error_rows):
    """Write the row indices of rows with errors.
    Input: list of row indices with errors
    Output: csv file with each item of dictionary on its own line.
    """
    with open("row_errors.csv", "w+", newline="") as csvfile:
        row_error_writer = csv.writer(csvfile, delimiter=",")
        for ind in error_rows:
            row_error_writer.writerow([ind])
