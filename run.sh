#!/bin/bash

echo "The pwd is:"
pwd
echo "The input directory has:"
ls ./input/
echo "The src dir has the following:"
ls ./src/

python3.7 ./src/pipeline.py ./input/censustract-00-10.csv ./output/report.csv

