import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

df= pd.read_csv('20181129_polution_simple.csv', sep=',', header=None)
# data= np.genfromtxt("20181128_idx.csv", dtype=float, delimiter=',', skip_header=1)

# arr= df.T.values 
# arr= df.values.T 
arr= df.values
print(arr)
print(arr.shape)

data= arr[:, 1:][1:]    # get all from 2nd col (col1) and remove row0
print(data)

len= len(data) 
print(len)

time0= arr[:, 0][1:]     # get col0 then get col1 (row1 & col0 from original source) & after
time= ((time0+ " ") * len) # repeat len(data) times to match 7 data cols 
print(time)

plt.plot(time, data)
plt.show()

# six= arr[:, 1:][1]    # only row1 (2nd)
# print(six)

# len= len(data)
# for i in range(len):
#      print(data[i])
