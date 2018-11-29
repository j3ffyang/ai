# import numpy as np 
# import pandas as pd 
from matplotlib import pyplot 
from mpl_toolkits.mplot3d import Axes3D
import random

fig= pyplot.figure()
ax= Axes3D(fig)

sequence_containing_x_vals= list(range(0, 100))
sequence_containing_y_vals= list(range(0, 100))
sequence_containing_z_vals= list(range(0, 100))

random.shuffle(sequence_containing_x_vals)
random.shuffle(sequence_containing_y_vals)
random.shuffle(sequence_containing_z_vals)

ax.scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals)


import numpy 

file= numpy.genfromtxt("20181128_idx.csv", delimiter=',')
x= file[:,1]
y= file[:,2]
z= file[:,3]

print(x)
print(y)
print(z)
# pyplot.show()

