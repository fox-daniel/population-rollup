import numpy as np
import csv

# GEOID,ST10,COU10,TRACT10,AREAL10,AREAW10,CSA09,CBSA09,CBSA_T,MDIV09,CSI,COFLG,POP00,HU00,POP10,HU10,NPCHG,PPCHG,NHCHG,PHCHG
# 01001020100,01,001,020100,3.787640715,0.01402014218,388,33860,"Montgomery, AL",,1,O,1906,764,1912,752,6,0.31,-12,-1.57

path_to_ouput = "./synthdata.csv"


def data_synth(path_to_ouput, num_rows):
    """Generate synthetic data and write to csv."""
    num_rows = num_rows
    col_names = [
        "GEOID",
        "ST10",
        "COU10",
        "TRACT10",
        "AREAL10",
        "AREAW10",
        "CSA09",
        "CBSA09",
        "CBSA_T",
        "MDIV09",
        "CSI",
        "COFLG",
        "POP00",
        "HU00",
        "POP10",
        "HU10",
        "NPCHG",
        "PPCHG",
        "NHCHG",
        "PHCHG",
    ]
    col_specs = [
        (int, 11),
        (int, 2),
        (int, 3),
        (int, 6),
        (float, None),
        (float, None),
        (int, 3),
        (int, 5),
        (str, None),
        ("any", None),
        (int, None),
        (str, None),
        (int, None),
        (int, None),
        (int, None),
        (int, None),
        (int, None),
        (float, None),
        (int, None),
        (float, None),
    ]
    name_specs = dict(zip(col_names, col_specs))

    with open(path_to_ouput, "w", newline="") as synthdata:
        synthwriter = csv.writer(synthdata, delimiter=",")
        synthwriter.writerow(col_names)
        for i in range(num_rows):
            row = []
            for name in name_specs.keys():
                if (name_specs[name][0] == int) and (name_specs[name][1] is not None):
                    num_min = 10 ** (name_specs[name][1] - 1)
                    num_max = 10 ** name_specs[name][1] - 1
                    value = np.random.randint(num_min, num_max)
                elif (name_specs[name][0] == int) and (name_specs[name][1] is None):
                    num_min = 0
                    num_max = 10 ** 5
                    value = np.random.randint(num_min, num_max)
                elif name_specs[name][0] == float:
                    num_min = 0
                    num_max = 10 ** 4
                    value = num_max * np.random.random()
                elif name_specs[name][0] == str:
                    value = "some, string"
                elif name_specs[name][0] == "any":
                    value = "mdiv09 value"
                row.append(value)
            synthwriter.writerow(row)
