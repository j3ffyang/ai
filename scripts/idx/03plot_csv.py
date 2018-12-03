import pandas as pd 
import matplotlib.pyplot as plt

from pandas_datareader import data

# df= pd.read_csv('20181129_polution.csv', sep=',', header=None)
df= data.DataReader('20181129_polution.csv', start='2018-11-01', end='2018-11-08', data_source=google)
print(df.values)

x= df.values[0, 1:]
# print(x)

# y= df.loc[:, 0]
y= df.values[1:, 0]
# print(y)

# z= df.loc[1:]
z= df.values[1:, 1:]
# print(z)

# plt.plot(x, z)
# plt.show()
