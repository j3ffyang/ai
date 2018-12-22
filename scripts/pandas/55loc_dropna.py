# https://www.udemy.com/learn-data-analysis-using-pandas-and-python/learn/v4/

import pandas as pd 

# pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns', None)

employee= pd.read_table("tab_separated_values.tsv")
print(employee)

# loc - choose a number of rows or cols 
print(employee.loc[0, :])
print(employee.loc[0:2, :])
print(employee.loc[0:2, ['Name', 'Position']])
print(employee.loc[0:2, 'Name':'Office'])

# missing data
employee1= pd.read_table("tab_separated_values_missing_values.tsv")
print(employee1.shape)

# drop rows with all missing value in every col
print(employee1.dropna(how= 'any').shape)
print(employee1.dropna(subset=['Name', 'Salary'], how= 'any').shape)
