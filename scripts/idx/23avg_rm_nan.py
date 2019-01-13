import pandas as pd 
import numpy as np

df= pd.read_csv("20181128_idx.csv")
print(df.values.shape)

data= df.values[:, 1:]  # all except 1st col (col0)
time= df.values[:, 0]   # 1st col (col0), which are dates

# data= data[~np.isnan(data)]
# data= pd.isnull(data)
data= data.ravel()      # multi dimensions into 1
data= [x for x in data if str(x) != 'nan']
# data= [x for x in data if ~np.isnan(x)]
print(data)

print(len(data))
# print(data.mean())
print(sum(data)/ float(len(data)))
