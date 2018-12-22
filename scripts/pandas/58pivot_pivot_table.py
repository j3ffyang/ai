# https://www.udemy.com/learn-data-analysis-using-pandas-and-python/learn/v4

import pandas as pd 

# basic pivoting
webtraffic= pd.read_csv("web_traffic.csv")
print(webtraffic)

wr2= webtraffic.pivot(index= "Page_Name", columns= "Date")
print(wr2)

# pivot tables 
# wr3= webtraffic.pivot_table(index= "Page_Name", aggfunc= "count") 
wr3= webtraffic.pivot_table(index= "Page_Name", aggfunc= "sum") 
print(wr3)
