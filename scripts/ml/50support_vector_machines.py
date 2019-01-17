from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt 

x, y= make_blobs(n_samples= 500, centers= 2,
        random_state= 0, cluster_std= 0.40)

import numpy as np 
xfit= np.linspace(-1, 3.5)

plt.scatter(x[:, 0], x[:, 1], c= y, s= 50, cmap= 'plasma')

for m, b, d in [(1, 0.65, 0.33), (0.5, 1.6, 0.55), (-0.2, 2.9, 0.2)]:
    yfit= m* xfit+ b
    plt.plot(xfit, yfit, '-k')
    plt.fill_between(xfit, yfit - d, yfit + d, edgecolor= 'none',
    color='#AFFEDC', alpha= 0.4)

plt.xlim(-1, 3.5)
plt.show()

