import csv
import population_funcs


# dictionaries {column_index, column_name} & {column_name, column_index}
path_to_csv = '../input/censustract-00-10.csv'
cols, cols_inds = population_funcs.create_column_dicts(path_to_csv)

select_cols= ['GEOID', 'ST10', 'COU10', 'TRACT10', 'CBSA09', 'CBSA_T', 'POP00', 'POP10', 'PPCHG']



# population_funcs.print_select_columns(select_cols, cols, cols_inds)

# num_rows = population_funcs.count_rows()
# print(num_rows)

# population_funcs.write_col_keys(cols)	