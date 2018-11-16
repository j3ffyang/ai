# https://scipython.com/book/chapter-6-numpy/examples/the-probability-of-cleaving-dna-with-ecori/

import numpy as np

lam = 12000 / 4**6
N = 100000
print(np.sum(np.random.poisson(lam, N)==0)/N)
