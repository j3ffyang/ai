
import pandas as pd

# read from tsv
employee = pd.read_table('./tab_separated_values.tsv')
print(employee.head())

# choose certain columns
employee = pd.read_table('./tab_separated_values.tsv')
cols = ['Name', 'Position']
print(employee[cols].head())

# choose certain rows
employee = pd.read_table('./tab_separated_values.tsv', nrows = 10)
print(employee[cols])

# display datatypes
employee = pd.read_table('./tab_separated_values.tsv')
print(employee.dtypes)

# display integer datatype
import numpy as np

employee = pd.read_table('./tab_separated_values.tsv')
print(employee.select_dtypes(include = [np.number]).dtypes)

# describe some inbuilt for data analysis
print(employee.describe())

# show # of rows and columns
print(employee.shape)

# type of object
print(type(employee))

# drop col
employee.drop('Office', axis = 1, inplace = True)
print(employee.head())

# concatenating 2 columns
employee['Name Salary'] = employee['Name'] + employee['Salary']
print(employee.head())

# reset
employee = pd.read_table('./tab_separated_values.tsv')
print(employee.head())

cols = ['Name', 'Position', 'Ofc', 'Age', 'StartDate', 'Sal']
employee.columns = cols
print(employee.head())

# reset
employee = pd.read_table('./tab_separated_values.tsv')

# sorting the data
# sort table by age
print(employee.sort_values(by = 'Age', ascending = False))

# sort a series
print(employee['Office'].sort_values())

# filtering and multi-filtering
# select all rows where age < 40
print(employee[employee.Age < 40])
print(employee[(employee.Age < 40) & (employee.Name == "Airi Satou")])

cols = ['Name', 'Position', 'Office']
print(employee[employee.Age < 40][cols].head())

# calculate mean
print(employee.mean())

# string manipulation
print(employee.Name.str.upper().head())
print(employee.Name.str.lower().head())

# select * where postition = software
print(employee.Position.str.contains('Software').head())
print(employee[employee.Position.str.contains('Software')])

# replace
print(employee.Position.str.replace('Engineer', 'Developer'))

# aggregations
print(employee.Age.min())
print(employee.Age.max())

# group by
print(employee.groupby('Position').Age.min())
print(employee.groupby('Position').Age.agg(['count', 'min', 'max']))

# Loc (choose a number of rows or columns)
employee = pd.read_table('./tab_separated_values.tsv')
print(employee.loc[0, :])

# row 0-2, all columns
print(employee.loc[0:2, :])

# row 0-2, 2 columns
print(employee.loc[0:2, ['Name', 'Position']])

# row 0-2, columns 0-3
print(employee.loc[0:2, 'Name':'Office'])

# rows with certain condition
print(employee.loc[employee.Position == 'Accountant', :])

# dropna. using missing value in tsv!!
# drop rows with all missing values in every columns
employee = pd.read_table('./tab_separated_values_missing_values.tsv')
print(employee.dropna(how="any").shape)

# drop rows with all missing values in certain columns
print(employee.dropna(subset=['Name', 'Salary'], how='any').shape)
