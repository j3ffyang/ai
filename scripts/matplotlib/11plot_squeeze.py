# https://stackoverflow.com/questions/42227997/how-to-plot-an-array-in-python

import numpy as np
import matplotlib.pyplot as plt

data = np.random.randint(3, 7, (10, 1, 1, 80))
newdata = np.squeeze(data) # Shape is now: (10, 80)
plt.plot(newdata) # plotting by columns
plt.show()
