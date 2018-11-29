import csv

results = []
with open("csvfile.csv") as csvfile:
    reader= csv.reader(csvfile, quoting= csv.QUOTE_NONNUMERIC) # change contents to float 
    for row in reader: # each row is a list 
        results.append(row)

print(results)
