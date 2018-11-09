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

## Getting a scalar value
print(df.loc[dates[0], 'A'])
print(df.at[dates[0], 'A'])

## selection by position
print(df.iloc[3])

## by integer slices, acting similar to numpy
print(df.iloc[3:5, 0:2])
print(df.iloc[[1,2,4], [0,2]])
print(df.iloc[1:3, :])
print(df.iloc[:, 1:3])

# getting a value explicitly
print(df.iloc[1,1])

# getting fast access to a scalar (equivalent to the prior method)
print(df.iat[1,1])

# Boolean indexing
## using a single column's values to select data
print(df[df.A > 0])

## selecting values from a DatFrame where a boolean condition is met
print(df[df > 0])

## using isin() method for filtering
df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
print(df2)

print(df2[df2['E'].isin(['two', 'four'])])

# Setting
## setting a new column automatically aligns the data by the indexes
s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))
print(s1)

## setting values by label
df.at[dates[0], 'A'] =0
## setting values by position
df.iat[0,1]= 0
## setting by assigning with a NumPy array
df.loc[:, 'D'] = np.array([5] * len(df))
print(df)

## A where operation with setting
df2 = df.copy()
df2[df2 > 0] = -df2
print(df2)

# Missing Data
## reindexing allows to change/ add/ delete the index on a specified axis.
df1 = df.reindex(index=dates[0:4], columns = list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1], 'E'] = 1
print(df1)

## dropping any rows that have missing data
print(df1.dropna(how= 'any'))

## filling missing data
print(df1.fillna(value=5))

## getting the boolean mask where values are nan
print(pd.isna(df1))

# Operations
## stats
print(df.mean())

## same operation on the other axis
print(df.mean(1))

## broadcasting along the specified dimension
s = pd.Series([1,3,5, np.nan, 6,8], index= dates.shift(2))
print(s)

print(df.sub(s, axis='index'))

## Apply
## applyting func to the data
print(df.apply(np.cumsum))
print(df.apply(lambda x: x.max() - x.min()))

## histogramming
s = pd.Series(np.random.randint(0, 7, size=10))
print(s)
print(s.value_counts())

## string methods
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print(s.str.lower())

## merge
## concat
df = pd.DataFrame(np.random.randn(10, 4))
print(df)

## break into pieces
pieces = [df[:3], df[3:7], df[7:]]
print(pd.concat(pieces))

## join
left = pd.DataFrame({'key': ['foo', 'bar'], 'lval':[1, 2]})
right= pd.DataFrame({'key': ['foo', 'bar'], 'rval':[4, 5]})

print(left)
print(right)

print(pd.merge(left, right, on='key'))

## append
df = pd.DataFrame(np.random.randn(8,4), columns=['A', 'B', 'C', 'D'])
print(df)

s = df.iloc[3]
print(df.append(s, ignore_index=True))

## Grouping
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                          'foo', 'bar', 'foo', 'bar'],
                   'B' : ['one', 'one', 'two', 'three',
                          'two', 'two', 'one', 'three'],
                   'C' : np.random.randn(8),
                   'D' : np.random.randn(8)})
print(df)
print(df.groupby('A').sum())
print(df.groupby(['A', 'B']).sum())

## Reshaping
