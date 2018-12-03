from numpy import * 
import matplotlib.pyplot as plt 

l_plot=[]

for i in range(10):
    x= arange(10)
    y= random.random(10)
    l_plot.append(plt.plot(x, y, '+-'))

plt.xlim(0, 12)
plt.legend([item[0] for item in l_plot], map(str, range(10))) 
plt.show()
