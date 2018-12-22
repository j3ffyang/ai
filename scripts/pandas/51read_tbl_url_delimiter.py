# https://www.udemy.com/learn-data-analysis-using-pandas-and-python/learn/v4/

import pandas as pd 

employee= pd.read_table("tab_separated_values.tsv")
print(employee.head())

a= pd.read_table("https://www.nrc.gov/reading-rm/doc-collections/event-status/reactor-status/2009/2009PowerStatus.txt", sep="|")
print(a.head())
