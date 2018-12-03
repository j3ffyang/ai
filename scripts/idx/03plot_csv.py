import datetime
import pandas as pd 
import matplotlib.pyplot as plt 

df= pd.read_csv('20181128_idx.csv')

# x= df.values[0, 1:]
# time= df.values[1:, 0]
time= list(df.Date)
a= list(df.Six)
b= list(df.Nine)
c= list(df.Ten_Thirty)
d= list(df.Thirteen_Thirty)
e= list(df.Sixteen_Thirty)
f= list(df.Ninteen_Thirty)
g= list(df.Twenty_One)

print(list(df))

fig= plt.figure()

plt.xlabel('Date')
plt.ylabel('Level')
plt.title('Sugar Level Monitoring')
plt.grid(True)

plt.plot_date(time, a, 'b-', label="6am")
# plt.plot_date(time, b, color='black')
plt.plot_date(time, c, 'g-')
plt.plot_date(time, d, color='orange')
plt.plot_date(time, e, 'r-')
plt.plot_date(time, f, 'y-')
plt.plot_date(time, g, 'c-')

fig.autofmt_xdate()
plt.show()
