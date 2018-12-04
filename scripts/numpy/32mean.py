import numpy as np 
import csv
from numpy import genfromtxt

data= csv.reader(open("winequality-red.csv"), delimiter=";")
wine= list(data)

qualities= [float(item[-1]) for item in wine[1:]]
mean= sum(qualities) / len(qualities)

print(mean)


