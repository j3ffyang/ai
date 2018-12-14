# https://www.dataquest.io/blog/numpy-tutorial-python/

import csv

with open("winequality-red.csv", 'r') as f:
    wines= list(csv.reader(f, delimiter=';'))

# print(wine) # entire array
print(wines[:3])   # first 3 lines

qualities= [float(item[-1]) for item in wines[1:]]
print(sum(qualities)/ len(qualities))
