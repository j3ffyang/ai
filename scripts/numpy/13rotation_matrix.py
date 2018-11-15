# https://scipython.com/book/chapter-6-numpy/examples/creating-a-rotation-matrix-in-numpy/

import numpy as np

theta= np.radians(30)
c, s= np.cos(theta), np.sin(theta)
R= np.array(((c, -s), (s, c)))
print(R)

R= np.array([[c, -s], [s, c]])
print(R)
