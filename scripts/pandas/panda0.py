import pandas as pd

# tsv file downloaded >
# https://datatables.net/extensions/buttons/examples/html5/tsv.html
employee = pd.read_table('./tab_separated_values.tsv')
print(employee.head())

# csv file downloaded from https://data-gov.tw.rpi.edu/wiki/CSV_files_use_delimiters_other_than_commas
# download from > https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2009/2009PowerStatus.txt

reads = pd.read_table('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2009/2009PowerStatus.txt', sep='|')
print(reads.head())
