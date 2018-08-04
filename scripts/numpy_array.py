import numpy as np

a = [[11,12,13], [21, 22, 23], [31, 32, 33]]

A = np.array(a)

print(A)
print(A.ndim)
print(A.shape)
print(A.size)

print(A[1][2])
print(A[0,0:2])

x = np.array([[1,0],[0,1]])
y = np.array([[2,1],[1,2]])

print(x + y)
print(2*y)
print(x * y)

print("***")

m = np.array([[0,1,1],[1,0,1]])
n = np.array([[1,1],[1,1],[-1,1]])
print(np.dot(m,n))

print("***")

p = np.array([0,1])
q = np.array([1,0])
print(np.dot(q,p))