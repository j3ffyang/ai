import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.ticker as mticker

df= pd.read_csv('20181128_idx.csv', sep=',', header=None)
# data= np.genfromtxt("20181128_idx.csv", dtype=float, delimiter=',', skip_header=1)

arr= df.values
print(arr)
print(arr.shape)

data= arr[:, 1:][1:]    # get all from 2nd col (col1) and remove row0
print(data.shape)

len= len(data[1])       # cause shape=[28,7], get len=2nd #
print(len)

data= data.ravel().astype(np.double)      # multi dimension into single dimension

time0= arr[:, 0][1:]    # get col0 then get col1 (row1 & col0 from original source) & after

time= []
for i in time0:
    for j in range(len):
        time.append(i+ str(j))

# fig= plt.figure(figsize=(16, 4))
fig, ax= plt.subplots(figsize=(16, 4))

plt.grid(True)
plt.xlabel('Date')
plt.ylabel('Level')
plt.title('All Monitoring')
ax.plot(time, data, linestyle='-', marker='o')
ax.xaxis.set_major_locator(mticker.MultipleLocator(7))

fig.autofmt_xdate()
plt.show()
