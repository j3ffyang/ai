# https://www.udemy.com/a-gentle-introduction-to-machine-learning-using-scikit-learn/learn/v4/t/lecture/6790082?start=0

from pandas import read_csv
from numpy import set_printoptions

filename= 'BBC.csv'
dataframe= read_csv(filename)
array= dataframe.values

import os 
print(os.getcwd())

print(dataframe.head(10))
print(dataframe.tail(10))

print(dataframe.shape)
print(dataframe.describe())

# create array
X= array[:, 0:11]
Y= array[:, 11]

# accuracy
print(dataframe.groupby('BikeBuyer').size())
