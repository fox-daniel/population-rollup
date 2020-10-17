import csv
from collections import defaultdict


def create_column_dicts(path_to_input):
    """Creates dictionaries: {column_index, column_name} and
    {column_name, column_index}"""
    cols = {}
    with open(path_to_input, newline="") as csvfile:
        inputreader = csv.reader(csvfile, delimiter=",")
        row = next(inputreader)
        for i, col in enumerate(row):
            cols[i] = col
    # dictionary {column_name, column_index}
    cols_inds = {v: k for k, v in cols.items()}
    return cols, cols_inds


def select_columns(path_to_input, path_to_ouput, selected_columns, cols, cols_inds):
    """Write the relevant columns to a new csv file."""
    with open(path_to_input, newline="") as inputfile:
        inputreader = csv.reader(inputfile, delimiter=",")
        with open(path_to_ouput, "w", newline="") as transfile:
            transwriter = csv.writer(transfile, delimiter=",")
            for row in inputreader:
                transwriter.writerow([row[cols_inds[col]] for col in selected_columns])


def clean_types(path_to_input, path_to_ouput, cols, cols_inds, col_types):
    """Clean types by formatting for appropriate type. Currently it
    removes quotes and commas from floats and ints.
    Column Types: int, int, str, int, int, float
    """

    def clean_type(astring, atype):
        """Cleans a string so that it is ready to be read as the appropriate type."""

        if atype == "int":
            """removes commas and quotes"""
            astring = astring.replace(",", "").replace('"', "")
            return astring

        if atype == "float":
            """removes commas and quotes"""
            astring = astring.replace(",", "").replace('"', "")
            return astring

        if atype == "str":
            return astring

    with open(path_to_input, newline="") as inputfile:
        inputreader = csv.reader(inputfile, delimiter=",")
        with open(path_to_ouput, "w", newline="") as transfile:
            transwriter = csv.writer(transfile, delimiter=",")
            row = next(inputreader)
            for row in inputreader:
                for i, atype in enumerate(col_types):
                    row[i] = clean_type(row[i], atype)
                transwriter.writerow(row)


# this will be simplified, with much of its functionality moved into separate functions
def groupby_cbsa(path_to_input, path_to_log, select_cols, cols, cols_inds):
    """
    Aggregate population data into CBSA's and return dictionaries with the CBSA09 code as the key.
    Input:
    path_to_input -  the path to csv file with the population data
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
    with open(path_to_log, "a", newline="") as errorfile:
        errorwriter = csv.writer(errorfile, delimiter=",")
        with open(path_to_input, newline="") as csvfile:
            inputreader = csv.reader(csvfile, delimiter=",")
            row = next(inputreader)
            i = 0
            for row in inputreader:
                try:
                    cbsa = row[cols_inds["CBSA09"]]
                    if cbsa != "":
                        cbsa_title[cbsa] = row[cols_inds["CBSA_T"]]
                        tract_count[cbsa] += 1
                        pop00_count[cbsa] += int(row[cols_inds["POP00"]])
                        pop10_count[cbsa] += int(row[cols_inds["POP10"]])
                        if row[cols_inds["PPCHG"]] == "(X)":
                            ppchg_avg[cbsa] = "(X)"
                        else:
                            ppchg_avg[cbsa] += float(row[cols_inds["PPCHG"]])
                except TypeError as err:
                    errorwriter.writerow(
                        ["TypeError: "] + [row[cols_inds[col]] for col in select_cols]
                    )
                except ValueError as err:
                    errorwriter.writerow(
                        ["ValueError: "] + [row[cols_inds[col]] for col in select_cols]
                    )
                i += 1
    for k, v in ppchg_avg.items():
        if ppchg_avg[k] != "(X)":
            ppchg_avg[k] = round(ppchg_avg[k] / tract_count[k], 2)
    return cbsa_title, tract_count, pop00_count, pop10_count, ppchg_avg, error_rows


def write_report(
    path_to_output,
    cols,
    cols_inds,
    cbsa_title,
    tract_count,
    pop00_count,
    pop10_count,
    ppchg_avg,
):
    with open(path_to_output, "w", newline="") as csvfile:
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
