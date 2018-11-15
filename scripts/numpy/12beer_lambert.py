# https://scipython.com/book/chapter-6-numpy/examples/fitting-the-beer-lambert-law-with-numpy/

import numpy as np
import pylab

# Path length, cm
path = 0.8
# The data: concentrations (M) and It/I0
c = np.array([0.4, 0.6, 0.8, 1.0, 1.2])
It_over_I0  = np.array([ 0.891 ,  0.841,  0.783,  0.744,  0.692])

n = len(c)
A = np.vstack((c, np.ones(n))).T
T = np.log(It_over_I0)

x, resid, _, _ = np.linalg.lstsq(A, T)
m, k = x
alpha = - m / path
print('alpha = {:.3f} M-1.cm-1'.format(alpha))
print('k', k)
print('rms residual = ', np.sqrt(resid[0]))

pylab.plot(c, T, 'o')
pylab.plot(c, m*c + k)
pylab.xlabel('$c\;/\mathrm{M}$')
pylab.ylabel('$\ln(I_\mathrm{t}/I_0)$')
pylab.show()
