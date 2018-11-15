# https://scipython.com/book/chapter-6-numpy/examples/mesh-analysis-of-a-electrical-network/

import numpy as np

R = np.matrix('50 0 -30; 0 40 -20; -30 -20 100')
V = np.matrix('80; 80; 0')
I = np.linalg.inv(R) * V

print(I)
