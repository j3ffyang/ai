import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

df= pd.read_csv("20181128_idx.csv")
print(df.values.shape)

chk_len = (df.values.shape[1]- 1)   # how many times of check per day

data= df.values[:, 1:]  # all except 1st col (col0)
time= df.values[:, 0]   # 1st col (col0)

new_time= []
for i in time:                       
    for j in range(chk_len):# repeat 7 date 
        new_time.append(i+ "-"+ str(j))  # its new_time, not time!

new_data= data.ravel()      # multi dimensions into 1
# forward-fill gap with NaN. limit=6 meaning 6 NaN
new_data= pd.Series(new_data).fillna(limit= 6, method= 'ffill')
# print(new_data)           # you can see the missing NaN replaced

# fig= plt.figure(figsize= (16, 4))
fig, ax= plt.subplots(figsize= (16, 4))

ax.grid(True)
ax.plot(new_time, new_data)
# ax.locator_params(nbins= 40, axis= 'x')
fig.autofmt_xdate()
plt.show()
