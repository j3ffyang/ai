from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# make data
x = np.linspace(-2, 2, 200)
y = x
x, y = np.meshgrid(x, y)
z = 50 - x**2 - y**2

# plot the surface
# plot a basic wireframe
surf = ax.plot_wireframe(x, y, z, rstride = 10, cstride = 10)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
