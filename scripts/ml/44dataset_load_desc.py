# https://data-flair.training/blogs/train-test-set-in-python-ml/
# https://archive.ics.uci.edu/ml/datasets/Forest+Fires
# https://github.com/Azure/Azure-MachineLearning-ClientLibrary-R/blob/master/demo/forestfires.csv

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

data= pd.read_csv('forestfires.csv')
print(data.head())
print(data.describe)
