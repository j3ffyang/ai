
import pandas as pd

# pipe delimited (name, etc)
# https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2009/2009PowerStatus.txt

reads = pd.read_table('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2009/2009PowerStatus.txt')
print(reads.head())

# delimited by "|" in original file. Remove them
reads = pd.read_table('https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2009/2009PowerStatus.txt', sep = "|")
print(reads.head())
