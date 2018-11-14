# https://scipython.com/book/chapter-6-numpy/examples/ 

import numpy as np

N, n = 101, 5
def f(i):
    return (i % n == 0) * 1

comb = np.fromfunction(f, (N,), dtype = int)
print(comb)
