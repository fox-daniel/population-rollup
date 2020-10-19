# test_scaling_file_size

This is the beginning of a test. Given more time, to develop it I would plot run time of pipeline.py against the number of rows in the csv of synthetic data. This would produce a threshold for when the current data structures and algorithms become impractical. If there were relevant use cases that exceeded the threshold then I would revise the pipeline to 1) write and read from csv less frequently and 2) use parquet files. 

### To test how pipeline.py scales with file size:
- cp test_scaling_file_size.py to the top-level directory 
- $python3.7 test_scaling_file_size.py
- logs are written to test_log.csv in this test directory