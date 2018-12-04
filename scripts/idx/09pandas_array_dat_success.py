# import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
# from matplotlib import pyplot

df= pd.read_csv('20181128_idx.csv', sep=',', header=None)
# data= np.genfromtxt("20181128_idx.csv", dtype=float, delimiter=',', skip_header=1)

# arr= df.T.values 
arr= df.values.T
print(arr.shape)

x= (arr[0])         # all col of date, which is the 1st col
x1= x[1:]           # from 2nd col
print(x1)

# six= (arr[1])
six= (arr[1][2:])   # 1= the 2nd row in arr. 2:= from 3rd col to the end
print(six)          # all col of six

plt.plot(x1, six, marker='o-')
plt.show()
