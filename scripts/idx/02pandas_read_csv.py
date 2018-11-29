import pandas as pd 

df= pd.read_csv('20181128_idx.csv', sep=',', header=None)
print(df.values)
