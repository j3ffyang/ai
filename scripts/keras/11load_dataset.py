# https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/

from keras.models import Sequential
from keras.layers import Dense 
import numpy 

# fix random seed for reproducibility 
# numpy.random.seed(7)

# load pima indians dataset 
dataset= numpy.loadtxt("pima-indians-diabetes.csv", delimiter= ",")
print(dataset.shape)

# split into input (X) and output (Y) vars 
X= dataset[:, 0:8]  # select col 0- 7, stop before col 8
Y= dataset[:, 8]    # indicator of diabetes result

print(X)
print(Y)
