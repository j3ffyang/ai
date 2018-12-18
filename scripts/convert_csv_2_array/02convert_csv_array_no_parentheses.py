import csv

results = []
with open('csvfile.csv') as f:
    output = [float(s) for line in f.readlines() for s in line[:-1].split(',')]
    print(output);
