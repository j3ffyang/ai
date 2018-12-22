# https://www.udemy.com/learn-data-analysis-using-pandas-and-python/learn/v4/

import pandas as pd 

# pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns', None)

employee= pd.read_table("tab_separated_values.tsv")

# mean
print(employee.mean())

# upper & lower
print(employee.Name.str.upper().head())
print(employee.Name.str.lower().head())

# select with condition like a sql
print(employee.Position.str.contains('Software'))
print(employee[employee.Position.str.contains('Software')])

# replace with condition
print(employee.Position.str.replace('Engineer', 'Developer'))

# aggregation
print(employee.Age.min())
print(employee.Age.max())

# group by with aggregation
print(employee.groupby('Position').Age.min())
print(employee.groupby('Position').Age.agg(['count', 'min', 'max']))
