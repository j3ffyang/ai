# import numpy as np 
import pandas as pd
from matplotlib import pyplot

df= pd.read_csv('20181128_idx.csv', sep=',', header=None)
# data= np.genfromtxt("20181128_idx.csv", dtype=float, delimiter=',', skip_header=1)

# arr= df.T.values 
arr= df.values.T
print(arr.shape)

x= (arr[0])   # all col of date
x1= x[1:]
print(x1)

# six= (arr[1])
six= (arr[1][2:])
print(six)
