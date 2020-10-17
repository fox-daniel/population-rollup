#!/bin/bash

git clone https://github.com/fox-daniel/population-rollup pop_roll_test

cd ./pop_roll_test

# Test_1
# cp ./insight_testsuite/tests/test_1/input/censustract-00-10.csv ./input/

./run.sh

# rm ./input/censustract-00-10.csv
cat ./output/report.csv
