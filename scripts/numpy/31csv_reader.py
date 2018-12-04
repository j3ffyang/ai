# https://www.dataquest.io/blog/numpy-tutorial-python/

import numpy as np 
import csv
from numpy import genfromtxt

# data= csv.reader(open("winequality-red.csv"), delimiter=";")
# with open("winequality-red.csv", 'r') as data:

wine= genfromtxt('winequality-red.csv', dtype= float, delimiter=";", skip_header=1)
# wine= genfromtxt('winequality-red.csv', dtype= float, delimiter=";", names=True)

print(wine) # entire array
# print(wine[:3])   # first 3 lines
# print(wine[1:])
