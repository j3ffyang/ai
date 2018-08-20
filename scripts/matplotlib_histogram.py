import matplotlib.pyplot as plt
# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
# fig = Figure()
# canvas = FigureCanvas(fig)
#
# import numpy as np
# x = np.random.randn(10000)
#
# ax = fig.add_subplot(111)
#
# ax.hist(x, 100)
#
# ax.set_title('Normal distribution with $\mu=0, \sigma=1$')
# fig.savefig('matplotlib_histogram.png')

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(10000)
plt.hist(x, 100)
plt.title(r'Normal distribution with $\mu=0, \sigma=1$')
# plt.savefig('matplotlib_histogram.png')
plt.show()
