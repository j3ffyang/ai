# https://scipython.com/book/chapter-6-numpy/examples/covariance-with-npcov/

# Consider the matrix of 5 observations each of 3 variables, x0, x1 and x2
# whose observed values are held in the three rows of the array X:

import numpy as np

X = np.array([ [0.1, 0.3, 0.4, 0.8, 0.9],
               [3.2, 2.4, 2.4, 0.1, 5.5],
               [10., 8.2, 4.3, 2.6, 0.9]
             ])

print(np.cov(X))
