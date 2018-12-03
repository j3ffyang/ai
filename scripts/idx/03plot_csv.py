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

fig= plt.figure(figsize=(12, 4))    # fig's length, height

plt.xlabel('Date')
plt.ylabel('Level')
plt.title('Sugar Level Monitoring')
plt.grid(True)

plt.plot_date(time, a, 'b-', label="6am")
# plt.plot_date(time, b, color='black', lebel="9am")
plt.plot_date(time, c, 'g-', label="10:30am")
# plt.plot_date(time, d, color='magenta', label="1:30pm")
plt.plot_date(time, d, 'm-', label="1:30pm")
plt.plot_date(time, e, 'r-', label="4:30pm")
plt.plot_date(time, f, 'y-', label="7:30pm")
plt.plot_date(time, g, 'c-', label="9pm")

plt.legend(loc='upper left')    # label placement

fig.autofmt_xdate()
plt.show()
