import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

df= pd.read_csv('20181128_idx.csv', sep=',', header=None)
# df= pd.read_csv('20181129_polution_simple.csv', sep=',', header=None)
# data= np.genfromtxt("20181128_idx.csv", dtype=float, delimiter=',', skip_header=1)

arr= df.values
print(arr)
print(arr.shape)

data= arr[:, 1:][1:]    # get all from 2nd col (col1) and remove row0
print(data.shape)

len= len(data[1])       # cause shape=[28,7], get len=2nd #
print(len)

data= data.ravel()      # multi dimension into single dimension
print(data)

time0= arr[:, 0][1:]    # get col0 then get col1 (row1 & col0 from original source) & after

time= []
for i in time0:
    for j in range(len):
        # time.append(i)+ str.format(i)
        time.append(i)
# print(time)

fig= plt.figure(figsize=(16, 4))
plt.plot(time, data, marker='o')
plt.show()
