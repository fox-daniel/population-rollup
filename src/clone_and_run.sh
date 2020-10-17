#!/bin/bash

git clone https://github.com/fox-daniel/population-rollup pop_roll_test


echo "****The pwd is ${PWD}.****"
cd ./pop_roll_test
echo "****After cd to repo, the pwd is ${PWD}.****"
echo "Next, execute: ./run.sh"
./run.sh