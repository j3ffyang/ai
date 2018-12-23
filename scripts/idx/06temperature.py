import pandas as pd  
from matplotlib import pyplot 

df= pd.read_csv('daily-minimum-temperatures-in-me.csv', sep=',', header=0, error_bad_lines= False)

print(df.head())
col2= df.loc[:, "Daily minimum temperatures in Melbourne, Australia, 1981-1990"]
print(col2.dtype)
converted= col2.convert_objects(convert_numeric= True)

col1= df.loc[:, "Date"]
col1.reindex(index=col1)
print(col1)

df.plot(col1, converted, style='k.')
pyplot.show()
