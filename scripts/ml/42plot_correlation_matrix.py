# https://data-flair.training/blogs/python-ml-data-preprocessing/#

import pandas, scipy, numpy
from sklearn.preprocessing import LabelEncoder

df= pandas.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv', sep= ';')

array= df.values

# separating data into input and output components
x= array[:, 0:8]
y= array[:, 8]

import matplotlib.pyplot as plt
correlations= df.corr()
fig= plt.figure()
ax= fig.add_subplot(111)
cax= ax.matshow(correlations, vmin= -1, vmax= 1)
fig.colorbar(cax)

ticks= numpy.arange(0, 9, 1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)

plt.show()
