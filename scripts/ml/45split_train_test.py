# https://data-flair.training/blogs/train-test-set-in-python-ml/
# https://archive.ics.uci.edu/ml/datasets/Forest+Fires
# https://github.com/Azure/Azure-MachineLearning-ClientLibrary-R/blob/master/demo/forestfires.csv

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

data= pd.read_csv('forestfires.csv')
# print(data.values)
# print(data.describe())

y= data.temp
x= data.drop('temp', axis= 1)

x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.2)
print(x_train.head())
print(x_train.shape)
print(x_test.head())
print(x_test.shape)
