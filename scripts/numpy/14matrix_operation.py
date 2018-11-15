# https://scipython.com/book/chapter-6-numpy/examples/matrix-operations/

import numpy as np

B= np.matrix([[1, 3-1j], [3j, -1+ 1j]])
print(B)

print(B.T)

print(B.H)

print(B.I)

print(np.trace(B))

print(np.linalg.det(B))
