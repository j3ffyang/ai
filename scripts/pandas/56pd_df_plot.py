# https://www.udemy.com/learn-data-analysis-using-pandas-and-python/learn/v4

import pandas as pd 
import matplotlib.pyplot as plt

df= pd.read_csv("monthly-milk-production-pounds-p.csv")
print(df.shape)
print(df.head())
# data= df.astype('float')

df.plot()
plt.show()
