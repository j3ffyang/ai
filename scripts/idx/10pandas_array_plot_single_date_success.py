import pandas as pd 
import matplotlib.pyplot as plt

df= pd.read_csv('20181129_polution.csv', sep=',', header=None)
# data= np.genfromtxt("20181128_idx.csv", dtype=float, delimiter=',', skip_header=1)

# arr= df.T.values 
# arr= df.values.T 
arr= df.values
print(arr.shape)

date= arr[:, 0][1:] # get col0 then get col1 & after
print(date)

