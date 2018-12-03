import pandas as pd 
import matplotlib.pyplot as plt
import datetime

# polution= pd.read_csv('20181129_polution.csv', index_col=0, date_parser=parse)
df= pd.read_csv('20181129_polution.csv', index_col=0)

x= df.values[0, 1:]
y= df.values[1:, 0]

print(x)
print(y)

# plt.plot(x,y)
# plt.show()
