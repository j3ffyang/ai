# https://machinelearningmastery.com/reproducible-results-neural-networks-keras/

from pandas import DataFrame
from pandas import concat
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import mean_squared_error
 
# fit MLP to dataset and print error
def fit_model(X, y):
	# design network
	model = Sequential()
	model.add(Dense(10, input_dim=1))
	model.add(Dense(1))
	model.compile(loss='mean_squared_error', optimizer='adam')
	# fit network
	model.fit(X, y, epochs=100, batch_size=len(X), verbose=0)
	# forecast
	yhat = model.predict(X, verbose=0)
	print(mean_squared_error(y, yhat[:,0]))
 
# create sequence
length = 10
sequence = [i/float(length) for i in range(length)]
# create X/y pairs
df = DataFrame(sequence)
df = concat([df.shift(1), df], axis=1)
df.dropna(inplace=True)
# convert to MLP friendly format
values = df.values
X, y = values[:,0], values[:,1]
# repeat experiment
repeats = 10
for _ in range(repeats):
	fit_model(X, y)
