# https://www.dataquest.io/blog/numpy-tutorial-python/

import numpy as np 

data= np.genfromtxt("winequality-red.csv", dtype=float, delimiter=';', skip_header=1)

print(data[:, 11])
print(data[:, 11]+ 10)
print(data[:, 11]* 2)
print(data[:, 11]+ data[:, 11])

# multiply 'alcohol' by 'quality' to get the wine with the highest score
print(data[:, 10]* data[:, 11])

print(np.genfromtxt("winequality-red.csv", dtype=float, delimiter=';', names= True)[0])

# axis sum
print(data.sum(axis=0))
print(data.sum(axis=0).shape)
print(data.sum(axis=1))

# comparison
print(data[:11]> 5)

high_quality= data[:, 11]> 7
# print(high_quality)
print(data[high_quality, :][:3, :])

# reshape with transpose: row-> col; col-> row 
print(np.transpose(data).shape)

# turn into 1 dimention array 
print(data.ravel())
