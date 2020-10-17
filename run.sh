#!/bin/bash

echo "The pwd is:"
pwd
echo "The input directory has:"
ls ./input/
echo "The src dir has the following:"
ls ./src/

python3.7 ./src/pipeline.py ./input/complaints.csv ./output/report.csv

