import pandas as pd 
import numpy as np
from matplotlib import pyplot

df= pd.read_csv('20181128_idx.csv', sep=',', header=None)
# print(df.values)

date= df.values[1:, 0]
time= df.values[0, 1:]

x= date+ time

y= df.values[0, 1:]

