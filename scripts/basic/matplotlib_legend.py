import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y1 = x**2
y2 = 2*x + 1

plt.figure(num=3, figsize=(8,5))

plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('I am x')
plt.ylabel('I am y')

new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.23, 3],
            [r'$really\ bad$', r'$bad\ \alpha$', r'$normal\ \beta$', 'good', 'very good']
            )

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

line1, = plt.plot(x,y2, label='up')
line2, = plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--', label='down')
plt.legend(handles=[line1, line2], labels=['aaa', 'bbb'], loc='best')

plt.show()
