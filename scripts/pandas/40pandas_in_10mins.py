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
## stack
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                     'foo', 'foo', 'qux', 'quz'],
                    ['one', 'two', 'one', 'two',
                     'one', 'two', 'one', 'two']]))

index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
df2 = df[:4]
print(df2)

## stack() method "compresses" a level in the DataFrame's columns
stacked = df2.stack()
print(stacked)

## the inverse operation of stack()
print(stacked.unstack())
print(stacked.unstack(1))
print(stacked.unstack(0))

## pivot tables
df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
                   'B': ['A', 'B', 'C'] * 4,
                   'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                   'D': np.random.randn(12),
                   'E': np.random.randn(12)})
print(df)

## we can product pivot tables from this data very easily
print(pd.pivot_table(df, values='D', index= ['A', 'B'], columns= ['C']))

## Time Series
rng = pd.date_range('1/1/2012', periods= 100, freq= 'S')
ts =  pd.Series(np.random.randint(0, 500, len(rng)), index= rng)
print(ts.resample('5Min').sum())

## time zone representation
rng = pd.date_range('3/6/2012 00:00', periods= 5, freq= 'D')
ts = pd.Series(np.random.randn(len(rng)), rng)
print(ts)

ts_utc = ts.tz_localize('UTC')
print(ts_utc)

## converting to another tiem zone
print(ts_utc.tz_convert('US/Eastern'))

## converting between time span representations
rng = pd.date_range('1/1/2012', periods= 5, freq= 'M')
ts = pd.Series(np.random.randn(len(rng)), index= rng)
print(ts)

ps = ts.to_period()
print(ps)

print(ps.to_timestamp())

## Categorical
df = pd.DataFrame({"id":[1,2,3,4,5,6], "raw_grade":['a','b','b','a','a','e']})

## convert the raw grades to a categorical data type
df["grade"] = df["raw_grade"].astype("category")
print(df["grade"])

## sort
print(df.sort_values(by="grade"))


## Plotting
# import matplotlib.pyplot as plt
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
plt.plot(ts)
plt.show()

## on a DataFrame, the plot() method is a convenience to plot all of the col w/ labels
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
                  columns= ['A', 'B', 'C', 'D'])
df = df.cumsum()

plt.figure(); plt.plot(df); plt.legend(loc = 'best')
plt.show()

## getting data in/ out
## csv
df.to_csv('40pandas_in_10mins_foo.csv')
print(pd.read_csv('40pandas_in_10mins_foo.csv'))

## excel
print(df.to_excel('40pandas_in_10mins_foo.xlsx', sheet_name='Sheet1'))
print(pd.read_excel('40pandas_in_10mins_foo.xlsx', 'Sheet1', index_col= None, na_values=['NA']))
