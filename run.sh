#!/bin/bash

cat ./input/complaints.csv

python3.7 ./src/pipeline.py ./input/complaints.csv ./output/report.csv

