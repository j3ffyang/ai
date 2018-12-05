import pandas as pd 
import matplotlib.pyplot as plt

df= pd.read_csv('20181128_idx.csv', sep=',', header=None)
# data= np.genfromtxt("20181128_idx.csv", dtype=float, delimiter=',', skip_header=1)

# arr= df.T.values 
arr= df.values.T
print(arr)
print(arr.shape)

x0= (arr[0])        # all col of date, which is the 1st col
x= x0[1:]           # from 2nd col 
print(x)

six0= (arr[1][1:])  # 1= the 2nd row in arr. 1:= from 2nd col to the end
six= pd.to_numeric(six0)    # change datatype from string to num 
print(six)          # all col of six 

nine= pd.to_numeric(arr[2][1:]) # 2= 3rd row
print(nine)

# fig= plt.figure(figsize=(12, 4))
# plt.plot(x, six, marker='o')
# plt.show()
