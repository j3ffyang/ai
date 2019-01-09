# https://data-flair.training/blogs/train-test-set-in-python-ml/

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

iris= load_iris()
x, y= iris.data, iris.target
x_train, x_test, y_train, y_test= train_test_split(x, y, train_size= 0.5,
        test_size= 0.5, random_state= 123)
print(y_test)
print(y_train)
