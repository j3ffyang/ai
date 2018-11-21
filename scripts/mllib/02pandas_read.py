# https://www.udemy.com/the-top-5-machine-learning-libraries-in-python/learn/v4/t/lecture/

import pandas as pd 

ufo= pd.read_table('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv', sep=',')

print(ufo.head())

print(ufo['State'])
ufo['Location']= ufo.City+ ', '+ ufo.State 
print(ufo.head())

print(ufo.shape)
print(ufo.dtypes)
print(ufo.columns)
