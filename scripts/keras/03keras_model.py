# https://www.udemy.com/a-gentle-introduction-to-deep-learning-using-keras/learn/v4/t/lecture/6834662?start=0

from keras.models import Sequential
from keras.layers import Dense
import numpy

seed= 9
numpy.random.seed(seed)

from pandas import read_csv
filename= 'BBCN.csv'
dataframe= read_csv(filename)

# create an array
array= dataframe.values

x= array[:, 0:11]
y= array[:, 11]

# check the data 
print(dataframe.head())

# build the model
model= Sequential()
model.add(Dense(12, input_dim=11, kernel_initializer='uniform', activation='relu'))
model.add(Dense(8, kernel_initializer='uniform', activation='relu'))
model.add(Dense(1, kernel_initializer='uniform', activation='sigmoid'))

# compile the model 
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# fit the model 
model.fit(x, y, nb_epoch= 500, batch_size= 10)

# score the model 
scores= model.evaluate(x, y)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]* 100))
