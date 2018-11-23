# https://www.udemy.com/a-gentle-introduction-to-deep-learning-using-keras/learn/v4/t/lecture/6834662?start=0

from keras.models import Sequential
from keras.layers import Dense
import numpy as np 

from pandas import read_csv
filename= 'BBC.csv'
dataframe= read_csv(filename)

array= dataframe.values

x= array[:, 0:11]
y= array[:, 11]

model= Sequential()
model.add(Dense(11, input_dim=11, kernel_initializer='uniform', activation='relu'))
model.add(Dense(8, kernel_initializer='uniform', activation='relu'))
model.add(Dense(8, kernel_initializer='uniform', activation='relu'))
model.add(Dense(1, kernel_initializer='uniform', activation='sigmoid'))
