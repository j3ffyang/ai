# working with plots

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./monthly-milk-production-pounds-p.csv')
print(data.head())

data.plot()
plt.show()
