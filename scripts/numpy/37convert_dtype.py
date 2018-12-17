# https://www.dataquest.io/blog/numpy-tutorial-python/

import numpy as np 

data= np.genfromtxt("winequality-red.csv", dtype=float, delimiter=';', skip_header=1)

data1= data.astype(int)
print(data1)
print(data.dtype.name)
print(data1.dtype.name)
