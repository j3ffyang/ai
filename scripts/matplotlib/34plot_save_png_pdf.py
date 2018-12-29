# https://www.datacamp.com/community/tutorials/matplotlib-tutorial-python

import matplotlib.pyplot as plt 
import numpy as np 

x= np.linspace(0, 10, 100)
plt.plot(x, x, label='linear')

plt.legend()
plt.show()

# plt.savefig("foo.png")
# plt.savefig("foo.png", transparent= True)

from matplotlib.backends.backend_pdf import PdfPages 
# pp= PdfPages('multipage.pdf')
# pp.savefig()
# pp.close()

