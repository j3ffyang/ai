# 10 mins to pandas
# https://pandas.pydata.org/pandas-docs/stable/10min.html

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Object creation
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

dates = pd.date_range('20130101', periods = 6)
print(dates)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)

df2 = pd.DataFrame({ 'A' :1.,
                     'B' : pd.Timestamp('20130102'),
                     'C' : pd.Series(1, index=list(range(4)), dtype='float32'),
                     'D' : np.array([3] * 4, dtype='int32'),
                     'E' : pd.Categorical(["test", "train", "test", "train"]),
                     'F' : 'foo' })
print(df2)

print(df2.dtypes)

# Viewing data
print(df.head())
print(df.tail(3))

print(df.index)
print(df.columns)
print(df.values)

print(df.describe())

## Transposing your data
print(df.T)

## Sorting by an axis
print(df.sort_index(axis=1, ascending=False))

## Sorting by values
print(df.sort_values(by='B'))

# Selection

## Getting by column
print(df['A'])

## Selecting via [], which slices the rows
print(df[0:3])

print(df['20130102':'20130104'])

## Selection by label
print(df.loc[dates[0]])

## Selecting on a multi-axis by label
print(df.loc[:, ['A', 'B']])

print(df.loc['20130102':'20130104', ['A', 'B']])

print(df.loc['20130102', ['A', 'B']])

print(df.loc[dates[0], 'A'])
print(df.at[dates[0], 'A'])
