# https://www.dataquest.io/blog/numpy-tutorial-python/

import numpy as np 
import csv
from numpy import genfromtxt

# alternative to tutorial
# data= csv.reader(open("winequality-red.csv"), delimiter=";")
# with open("winequality-red.csv", 'r') as data:

# wines= genfromtxt('winequality-red.csv', dtype= float, delimiter=";", skip_header=1)
wines= genfromtxt('winequality-red.csv', dtype= float, delimiter=";", names=True)

print(wines) # entire array. all in one row!
print(wines[:2])   # first 2 lines
print(wines[2:2])   
print(wines[2:])   
