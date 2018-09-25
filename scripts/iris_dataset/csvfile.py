import csv

with open('iris.data', 'r') as csvfile:
    lines = csv.reader(csvfile)
    for row in lines:
        print(', '.join(row))


# from urllib.request import urlopen
#
# lines = urlopen("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
# lines = map(lambda s: s.strip(), lines)
#
# for row in lines:
    # print(', '.join(row))
    # print(row)
