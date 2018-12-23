import pandas as pd 

df= pd.read_csv("20181128_idx.csv")
print(df)

time= df["Date"]
print(time)

