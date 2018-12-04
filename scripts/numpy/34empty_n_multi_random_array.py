import numpy as np 

empty_array= np.zeros((3, 4))
print(empty_array)

print("=-=-=-=-")

x= np.random.rand(3, 4) # create an array of 3 rows and 4 cols
print(x)

print("=-=-=-=-")

y= np.random.rand(2,3,4,5)  # create an array in 4 dimensions
print(y)
print(y.shape)

