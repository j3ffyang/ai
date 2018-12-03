import pandas as pd  
from matplotlib import pyplot 

# series= pd.read_csv('daily-minimum-temperatures-in-me.csv', sep=',', header=0)
series= pd.read_csv('daily-minimum-temperatures-in-me.csv')

print(series.head())
# series.plot(style='k.')
# pyplot.show()
