# https://scipython.com/book/chapter-6-numpy/examples/finding-a-best-fit-straight-line/

import numpy as np
import pylab
Polynomial = np.polynomial.Polynomial

# the data: conc= [P] and absorbance, A
conc= np.array([0, 20, 40, 80, 120, 180, 260, 400, 800, 1500])
A= np.array([2.287, 3.528, 4.336, 6.909, 8.274, 12.855, 16.085, 24.797,
             49.058, 89.400])

cmin, cmax= min(conc), max(conc)
pfit, stats= Polynomial.fit(conc, A, 1, full= True, window= (cmin, cmax),
                                                    domain= (cmin, cmax))

print('Raw fit results:', pfit, stats, sep='\n')

A0, m= pfit
resid, rank, sing_val, rcond= stats
rms= np.sqrt(resid[0]/ len(A))

print('Fit: A= {:.3f}[P]+ {:.3f}'.format(m, A0),
      '(rms residual= {:.4f})'.format(rms))

pylab.plot(conc, A, 'o', color= 'k')
pylab.plot(conc, pfit(conc), color='k')
pylab.xlabel('[P] /$\mathrm{\mu g\cdot mL^{-1}}$')
pylab.ylabel('Absorbance')
pylab.show()
