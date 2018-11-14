# https://scipython.com/book/chapter-6-numpy/examples/the-correlation-between-air-pressure-and-temperature/
# cvs > https://www.cl.cam.ac.uk/research/dtg/weather/weather-raw.csv

# the following program determines the correlation co-efficient between
# pressure and temperature

import numpy as np
import pylab

data= np.genfromtxt('weather-raw.csv', delimiter=',', usecols=(1,4))

# remove any rows with either missing T or missing p
data= data[~np.any(np.isnan(data), axis= 1)]

# temperatures are reported after multiplication by a factor of 10 so remove it
data[:,0] /= 10

# get the correlation coefficient
corr= np.corrcoef(data, rowvar=0)[0,1]
print('p-T correlation coefficient: {:.4f}'.format(corr))

# plot the data: T on x, p on y
pylab.scatter(*data.T, marker='.')
pylab.xlabel('$T$ /$\mathrm{^\circ C}$')
pylab.ylabel('$p$ /mbar')
pylab.show()
