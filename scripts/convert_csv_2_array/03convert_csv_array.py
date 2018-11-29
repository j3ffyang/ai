import csv

results = []
with open('csvfile.csv', 'rt') as csvfile:
# with open('csvfile.csv', 'rb') as csvfile:
# with open('csvfile.csv') as csvfile:
    reader= csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        results.append(row)

print(results)
