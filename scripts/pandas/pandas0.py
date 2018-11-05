import pandas as pd
import numpy as np

# tsv file downloaded >
# https://datatables.net/extensions/buttons/examples/html5/tsv.html

cols = ['Name', 'Position']
employee = pd.read_table('./tab_separated_values.tsv')
# employee = pd.read_table('./tab_separated_values.tsv', nrows= 4)
print(employee[cols].head())
# print(employee.head())
# print(employee.dtypes)
print(employee.select_dtypes(include = [np.number]).dtypes)
print(employee.describe())

# csv file downloaded from https://data-gov.tw.rpi.edu/wiki/CSV_files_use_delimiters_other_than_commas
# download from > https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2009/2009PowerStatus.txt

reads = pd.read_table('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2009/2009PowerStatus.txt', sep='|')
print(reads.head())
