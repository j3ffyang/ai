# pylab is module in patplotlib that get installed alongside matplotlib
# https://www.udemy.com/the-top-5-machine-learning-libraries-in-python/
import numpy as np 
import pylab as pl 

ds= np.random.normal(5.0, 3.0, 1000)

pl.hist(ds)
pl.xlabel('ds')
pl.show()

