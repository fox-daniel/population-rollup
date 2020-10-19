import csv
import sys
import os
import time

sys.path.append("./src/")
sys.path.append("./insight_testsuite/tests/test_scaling_file_size/")
import importlib
import validation
import transformation
from data_synth import data_synth

importlib.reload(validation)
importlib.reload(transformation)

path_to_output = "./input/censustract-00-10.csv"
path_to_log = "./insight_testsuite/tests/test_scaling_file_size/test_log.csv"


def main():
    """Test how pipeline.py scales with file size in terms of time and memory use.

    Execute this script from the top-level project directory.

    This script calls data_synth.py to generate synthetic data, to place it in the
    top level input folder, and to run pipeline.py on it. Timing and memory use metrics
    are collected and written to test_log.csv.
    """
    num_rows = 5

    data_synth(path_to_output, num_rows)
    with open(path_to_log, "w", newline="") as logfile:
        logwriter = csv.writer(logfile, delimiter=",")
        logwriter.writerow(
            [
                f"****Measure how pipeline.py scales with the number of rows in the input csv.****"
            ]
        )
        logwriter.writerow(
            [
                "Returned from test_scaling_file_size.py at {datetime.now().isoformat(timespec='seconds')}"
            ]
        )
        logwriter.writerow(["Number of Rows ----- Number of Seconds:"])
        for num_rows in range(10000, 10 ** 6, 10000):
            start = time.time()
            os.system("./run.sh")
            duration = time.time() - start
            logwriter.writerow([num_rows, duration])
        logwriter.writerow([])
        logwriter.writerow([])


if __name__ == "__main__":
    main()
