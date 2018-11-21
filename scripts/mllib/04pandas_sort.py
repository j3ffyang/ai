# https://www.udemy.com/the-top-5-machine-learning-libraries-in-python/learn/v4/t/lecture/

import pandas as pd 

ufo= pd.read_table('https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv', sep=',')

s= ufo.State.sort_values(ascending= False).head(20)
print(s)

t= ufo.sort_values('City')
print(t)

t1= ufo.sort_values(['City', 'State']).head(25)
print(t1)
