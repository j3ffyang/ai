# https://www.udemy.com/learn-data-analysis-using-pandas-and-python/learn/v4/

import pandas as pd 

# pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns', None)

employee= pd.read_table("tab_separated_values.tsv")

# sort tbl by age 
sort_by_age= employee.sort_values('Age', ascending= True)
print(sort_by_age.head())

# sort by office 
sort_by_office= employee.sort_values('Office', ascending= True)
print(sort_by_office.head())

# age < 40
print(employee[employee.Age < 40])
print(employee[(employee.Age < 40) & (employee.Name== "Airi Satou")])

cols= ['Name', 'Position']
print(employee[employee.Age< 40][cols].head())

