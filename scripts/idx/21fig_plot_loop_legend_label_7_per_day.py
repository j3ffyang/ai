import pandas as pd 
import matplotlib.pyplot as plt

df= pd.read_csv("20181128_idx.csv")
# df= pd.read_csv("20181128_idx.csv", sep=',', header=None)
data= df.values[:, 1:]  # from col1 to the end = all data 
print(data) 
len= len(data[1])       # 7 checks total per day= len of col

time= df.values[:, 0]   # all date 
print(time)

fig, ax= plt.figure(figsize= (14, 4))
for i in range(len):
    plt.plot(time, data[:, i], label= i+ 1) # i+1 = 7 sequential checks/day
plt.grid(True)
plt.xlabel('Date')
plt.ylabel('Level at particular time in a day')

set_xticks('Date'[::3])

fig.autofmt_xdate()
plt.legend()    # must exist or label won't appear
plt.show()
