# https://www.dataquest.io/blog/numpy-tutorial-python/

import numpy as np 
import csv
from numpy import genfromtxt

# data= genfromtxt('winequality-red.csv', delimiter=";")
# data= np.loadtxt("winequality-red.csv", delimiter=";")
# data= csv.reader(open("winequality-red.csv"), delimiter=";")
# with open("winequality-red.csv", 'r') as data:

with open("winequality-red.csv", 'r') as f:
    wine= list(f)

print(wine[:3])   # first 3 lines
# print(wine[1:])

