import pandas as pd 

df= pd.read_csv('20181129_polution.csv', sep=',', header=None)
print(df.values)
