# pylab is module in patplotlib that get installed alongside matplotlib
import numpy as np 
import pylab as pl 

ds= np.random.normal(5.0, 3.0, 1000)

pl.hist(ds)
pl.xlabel('ds')
pl.show()

