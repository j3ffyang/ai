import numpy as np 

empty_array= np.zeros((3, 4))
print(empty_array)

one_array= np.random.rand(6, 4)
print(one_array)

concatenate= np.concatenate((empty_array, one_array), axis= 0)
print(concatenate)

first_col= concatenate[:, 0]
print(first_col)
