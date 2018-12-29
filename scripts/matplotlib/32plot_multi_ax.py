import matplotlib.pyplot as plt 

fig= plt.figure(figsize=(10, 5))
ax1= fig.add_subplot(121)   # 1= axes lie horizontally, 2= 2 cols
ax2= fig.add_subplot(122)

ax1.bar([1,2,3], [3,4,5])
ax2.barh([0.5, 1, 2.5], [0, 1, 2])  # horizontal bar

plt.show()
