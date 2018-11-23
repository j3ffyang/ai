# https://www.udemy.com/a-gentle-introduction-to-deep-learning-using-keras/learn/v4/t/lecture/6838114?start=0

from keras.models import Sequential
from keras.layers import Dense
import numpy as np 

seed = 7
np.random.seed(seed)

from pandas import read_csv
filename= 'BBC.csv'
dataframe= read_csv(filename)

array= dataframe.values

x= array[:, 0:11]
y= array[:, 11]

print(x)
print(y)
