# https://www.udemy.com/learn-data-analysis-using-pandas-and-python/learn/v4/

import pandas as pd 

employee= pd.read_table("tab_separated_values.tsv")
print(employee.head())

# choose col
cols= ['Name', 'Position']
print(employee[cols])

# choose row 
employee= pd.read_table('tab_separated_values.tsv', nrows= 4)
print(employee)

# display dtype
employee= pd.read_table('tab_separated_values.tsv')
print(employee.dtypes)

# display int datatypes
import numpy as np
employee= pd.read_table('tab_separated_values.tsv')
print(employee.select_dtypes(include= [np.number]).dtypes)

# some built-in methods for data analysis 
print(employee.describe())

# show me the # of row/ col 
print(employee.shape)

# type of obj -> should be DataFrame
print(type(employee))
