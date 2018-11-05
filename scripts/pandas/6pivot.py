import pandas as pd

webtraffic = pd.read_csv('./web_traffic.csv')
print(webtraffic)

# pivot
print(webtraffic.pivot(index = "Page_Name", columns= "Date"))

# pivot table
print(webtraffic.pivot_table(index = "Page_Name", aggfunc = "sum"))

# pivot mean
print(webtraffic.pivot_table(index = "Page_Name", aggfunc = "mean"))

# pivot count
print(webtraffic.pivot_table(index = "Page_Name", aggfunc = "count"))
