import pandas as pd  
from matplotlib import pyplot 

import warnings
warnings.filterwarnings("ignore", category= FutureWarning)

df= pd.read_csv('daily-minimum-temperatures-in-me.csv', sep=',', header=0, error_bad_lines= False)

col2= df.loc[:, "Daily minimum temperatures in Melbourne, Australia, 1981-1990"]
print(col2.dtype)
converted= col2.convert_objects(convert_numeric= True)
print(converted.head())

col1= df.loc[:, "Date"]
print(col1.head())

# df.plot(col1, converted, style='k.')
# pyplot.show()
