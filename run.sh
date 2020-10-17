#!/bin/bash

# cp ./insight_testsuite/tests/test_1/input/censustract-00-10.csv ./input/
echo "The pwd is:"
pwd
echo "This directory has the following:"
ls -a
echo "The input directory has:"
ls ./input/
echo "The run.sh file looks like:"
cat run.sh
echo "The src dir has the following:"
ls ./src/
python3.7 ./src/pipeline.py ./input/censustract-00-10.csv ./output/report.csv

# rm ./input/censustract-00-10.csv
