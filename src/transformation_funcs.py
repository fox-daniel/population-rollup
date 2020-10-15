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
    ppchg_avg = defaultdict(float)
    error_rows = []
    with open(path_to_error_log, "w+", newline="") as errorfile:
        errorwriter = csv.writer(errorfile, delimiter=",")
        with open(path_to_csv, newline="") as csvfile:
            censusreader = csv.reader(csvfile, delimiter=",")
            row = next(censusreader)
            i = 0
            for row in censusreader:   
                if row[cols_inds["CBSA09"]] == "":
                    cbsa = 'None'+row[cols_inds["GEOID"]]
                else:
                    cbsa = row[cols_inds["CBSA09"]]
                if row[cols_inds["CBSA_T"]] == "":
                    cbsat = 'None'
                else:
                    cbsat = row[cols_inds["CBSA_T"]]
                try:
                    cbsa_title[cbsa] = cbsat                    
                    
                    tract_count[cbsa] += 1
                    pop00_count[cbsa] += int(
                        row[cols_inds["POP00"]]
                    )
                    pop10_count[cbsa] += int(
                        row[cols_inds["POP10"]]
                    )
                    if row[cols_inds["PPCHG"]] == '(X)':
                        ppchg_avg[cbsa] = '(X)'
                        # print('first conditional: ', ppchg_avg[cbsa])
                        # errorwriter.writerow(['ppchg is (X)']+[row[cols_inds[col]] for col in select_cols])
                    elif isinstance(row[cols_inds["PPCHG"]], str) & (ppchg_avg[cbsa] != '(X)'):
                        ppchg_avg[cbsa] += float(
                        row[cols_inds["PPCHG"]].replace(",",""))
                    elif isinstance(row[cols_inds["PPCHG"]], float) or isinstance(row[cols_inds["PPCHG"]], int):
                        ppchg_avg[cbsa] += float(
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
        for k in sorted(tract_count.keys()):
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
