# https://scipython.com/book/chapter-6-numpy/examples/modelling-the-distribution-of-mathrm13c-atoms-in-mathrmc_60/

import numpy as np

n, x = 60, 0.0107
mmax = 4
m = np.arange(mmax+1)

# Estimate the abundances by random sampling from the binomial distribution
ntrials = 10000
pbin = np.empty(mmax+1)
for r in m:
    pbin[r] = np.sum(np.random.binomial(n, x, ntrials)==r)/ntrials

# Calculate and store the binomial coefficients nCm
nCm = np.empty(mmax + 1)
nCm[0] = 1
for r in m[1:]:
    nCm[r] = nCm[r-1] * (n - r + 1)/ r
# The "exact" answer from binomial distribution
p = nCm * x**m * (1-x)**(n-m)

print('Abundances of C60 as (13C)[m](12C)[60-m]')
print('m   "Exact"    Estimated')
print('-'*24)
for r in m:
    print('{:1d}   {:6.4f}      {:6.4f}'.format(r, p[r], pbin[r]))
