# https://www.dataquest.io/blog/numpy-tutorial-python/

import numpy as np 

"""
with open("winequality-red.csv", 'r') as f:
    # wine= list(f)
    wine= np.array(list(f))
"""

# data= np.genfromtxt("winequality-red.csv", dtype=float, delimiter=',', names=True)
data= np.genfromtxt("winequality-red.csv", dtype=float, delimiter=';', skip_header=1)

print(data)
print(data.shape)

