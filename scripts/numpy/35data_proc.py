# https://www.dataquest.io/blog/numpy-tutorial-python/

import numpy as np 

# data= np.genfromtxt("winequality-red.csv", dtype=float, delimiter=',', names=True)
data= np.genfromtxt("winequality-red.csv", dtype=float, delimiter=';', skip_header=1)

# print(data.shape)
print(data[2, 3])   # row 3 and col 4
print(data[0:3, 3]) # first 3 rows and the 4th col
# print(data[:3, 3])    # same the above one 

print(data[:, 3])   # entire 3rd col / column
print(data[3, :])   # entire 4th row

data[1,2]= 10       # update value on row 2 and col 3 to 10
data[:, 10]= 10     # override entire 11th col
print(data)

# 1 dimention array
third_wine= data[3, :]
print(third_wine)
