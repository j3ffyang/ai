# https://data-flair.training/blogs/train-test-set-in-python-ml/

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression

iris= load_iris()
x, y= iris.data, iris.target
x_train, x_test, y_train, y_test= train_test_split(x, y, train_size= 0.5,
        test_size= 0.5, random_state= 123)

lm= LinearRegression()

model= lm.fit(x_train, y_train)
predictions= lm.predict(x_test)

import matplotlib.pyplot as plt 
plt.scatter(y_test, predictions)

plt.xlabel('True Values')
plt.ylabel('Predictions')


plt.show()
