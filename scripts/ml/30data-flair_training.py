# https://data-flair.training/blogs/python-ml-data-preprocessing/

import pandas, scipy, numpy
from sklearn.preprocessing import MinMaxScaler

df= pandas.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv', sep= ';')

print(df.describe)
