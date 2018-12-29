# https://www.datacamp.com/community/tutorials/matplotlib-tutorial-python

import matplotlib.pyplot as plt 

fig= plt.figure()
ax1= fig.add_subplot(131)
ax2= fig.add_subplot(132)
ax3= fig.add_subplot(133)

ax1.bar([1,2,3], [3,4,5])
ax2.barh([0.5,1,2.5], [0,1,2])
ax2.axhline(0.45)
ax1.axvline(1.0)
ax3.scatter(3, 4)

plt.show()
