import pandas as pd 

df1= pd.read_csv("./income_data.csv")
print(df1)

# df2= df1.set_index("State", drop= False)
df2= df1.set_index("State")
print(df2)

