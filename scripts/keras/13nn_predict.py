# https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/

#create 1st network with keras 
from keras.models import Sequential
from keras.layers import Dense 
import numpy 

# fix random seed for reproducibility 
seed= 7
numpy.random.seed(seed)

# load pima indians dataset 
dataset= numpy.loadtxt("pima-indians-diabetes.csv", delimiter= ",")

# split into input (X) and output (Y) vars 
X= dataset[:, 0:8]  # the first 7 cols before 8th 
Y= dataset[:, 8]    # the 8th col 

# create model 
model= Sequential()
model.add(Dense(12, input_dim= 8, init= 'uniform', activation= 'relu'))
model.add(Dense(8, init= 'uniform', activation= 'relu'))
model.add(Dense(1, init= 'uniform', activation= 'sigmoid'))

# compile model 
model.compile(loss= 'binary_crossentropy', optimizer= 'adam', metrics= ['accuracy'])

# fit the model 
# model.fit(X, Y, epochs= 150, batch_size= 10, verbose= 2)
model.fit(X, Y, epochs= 50, batch_size= 10, verbose= 2)

# calculate predictions 
predictions= model.predict(X)

# evaluate the model    # from previous script 
scores= model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]* 100))

# round predictions
rounded= [round(x[0]) for x in predictions]
print(rounded)

