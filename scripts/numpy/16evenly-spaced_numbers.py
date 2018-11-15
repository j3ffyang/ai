# https://scipython.com/book/chapter-6-numpy/examples/random-sampling-of-evenly-spaced-real-numbers/

import numpy as np

a, b, n= 0.5, 3.5, 4
print(a+ (b- a) * (np.random.random_integers(n)- 1)/ (n- 1.))
