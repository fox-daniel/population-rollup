# population_rollup

population_rollup computes aggregate statistics for Core Based Statistical Areas (CBSA) using input data at the level of census tracts from the 2000 and 2010 censuses of the United States. It is being submitted for the Coding Challenge of the Data Engineering track at Insight Data Science.

## Installation

From the directory in which you want the project to live, clone the repo.

```
git clone https://github.com/fox-daniel/population-rollup population_rollup
```
This will reproduce the project within the directory "population_rollup".

## Usage

Copy the file "censustract-00-10.csv" to /population_rollup/input.

From within the directory, population_rollup, run the following bash command.
```
./run.sh
```
The file "report.csv" will be written to /population_rollup/output.

The "run.sh" file runs the following command.
```
python3.7 ./src/pipeline.py ./input/censustract-00-10.csv ./output/report.csv
```
The variables for the script pipeline.py should be the paths (relative to population_rollup) to the input csv file and the output csv file.

### PPCH = '(X)'
When PP00 is 0 the PPCH is reported as infinite using the symbol '(X)'. This is done even if PP10 is also 0 even though in that case one could argue to report the PPCH as 0. When a CBSA contains a census tract for which PPCH is reported as '(X)', then the average PPCH over the CBSA is reported as '(X)' under the convention that infinity plus a finite number (or infinity) is infinity. Other reporting options might prove more useful. For example, the census tracts with PPCH = '(X)' could be dropped from the computation of the average. Another possibility would be to set PPCH = 0 if PP00 = PP10 = 0; this would apply to some CBSAs but still require a choice to be made when PP00 = 0 and PP10 > 0.

### test_type_test
This checks whether values in the csv can be converted to the appropriate data type. If an exception is raised this is written to a log.

### test_no_cbsa
This test runs an abbreviated version of the pipeline on a test csv in which the CBSA09 is missing for one of the two rows. The output correctly only reflects the single row with the CBSA09.

### test_row_length
This tests whether the row lengths remains constant.

### test_groupby_cbsa
This tests the groupby function which computes aggregate statistics. 

### test_geoid
This tests whether the GEOID is the concatenation of ST10, COU10,and TRACT10.

### Further Work
This code could be improved to scale better in the following ways.
- If large csv files are expected as input, then converting them to parquet files to store data during the inner stages of the pipeline should improve the speed.

## Contributing
This is a private repo.

## License

MIT License

Copyright (c) 2020 Daniel Fox

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

