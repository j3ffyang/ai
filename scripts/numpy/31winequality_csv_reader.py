# https://www.dataquest.io/blog/numpy-tutorial-python/

import csv
import numpy

with open("winequality-red.csv", 'r') as f:
    wines= list(csv.reader(f, delimiter=';'))

# print(wine) # entire array
print(wines[:3])   # first 3 lines

qualities= [float(item[-1]) for item in wines[1:]]

print("########")
print("Avg of Quality")
print(sum(qualities)/ len(qualities))

print("########")
print("Shape of Data")
print(numpy.shape(wines))
print(wines[1:2])
# print(wines[1:])
