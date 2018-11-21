# https://www.udemy.com/the-top-5-machine-learning-libraries-in-python/learn/v4/t/lecture/

import pandas as pd 

ufo= pd.read_table('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv', sep=',')

ufo.drop('Colors Reported', axis= 1, inplace= True)
print(ufo.head())
