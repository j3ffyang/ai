# https://www.udemy.com/learn-data-analysis-using-pandas-and-python/learn/v4

import pandas as pd 

df1= pd.DataFrame({
    "employee": ["ABC", "XYZ", "MNO"],
    "age": ["22", "25", "44"]
    })

df2= pd.DataFrame({
    "employee": ["ABC", "XYZ", "PQR"],
    "salary": ["10000", "125000", "30000"]
    })

# inner join 
df3= pd.merge(df1, df2, on= "employee") 
print(df3)

# outer join 
df4= pd.merge(df1, df2, on= "employee", how= "outer")
print(df4)

# left join 
df5= pd.merge(df1, df2, on= "employee", how= "left")
print(df5)
