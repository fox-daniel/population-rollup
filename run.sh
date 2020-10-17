#!/bin/bash

cp ./insight_testsuite/tests/test_1/input/censustract-00-10.csv ./input/

python3.7 ./src/pipeline.py ./input/censustract-00-10.csv ./output/report.csv

# rm ./input/censustract-00-10.csv
