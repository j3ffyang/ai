import pandas as pd 

df= pd.read_csv('20181129_polution.csv', sep=',', header=None)
print(df.values)

x= df.values[0, 1:]
y= df.values[1:, 0]
z= df.values[1:, 1:]

print(x.shape)
print(y.shape)
print(z.shape)

from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

fig= pyplot.figure()
ax= Axes3D(fig)

# ax.scatter(x, y, z)
# pyplot.show()
