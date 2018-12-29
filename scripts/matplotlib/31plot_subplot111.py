# https://www.datacamp.com/community/tutorials/matplotlib-tutorial-python

import matplotlib.pyplot as plt 
import numpy as np 

fig= plt.figure()
ax= fig.add_subplot(111)
ax.scatter(np.linspace(0, 1, 5), np.linspace(0, 5, 5))

plt.show()
