import numpy as np

# you have a 3x3 array to which you wish to add a row or col.
# adding a row with np.vstack
a = np.ones((3, 3))
print(np.vstack((a, np.array((2,2,2)))))

# adding a col with np.hstack
a = np.ones((3,3))
b = np.array((2,2,2)).reshape(3,1)
print(b)
print(np.hstack((a, b)))
