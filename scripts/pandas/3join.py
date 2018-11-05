
import pandas as pd

dataframe1 = pd.DataFrame({
    "employee": ["ABC", "XYZ", "MNO"],
    "age": ["22", "33", "44"]
})

print(dataframe1)

dataframe2 = pd.DataFrame({
    "employee": ["ABC", "XYZ", "PQR"],
    "salary": ["10000", "125000", "30000"]
})

# INNER join
dataframe3 = pd.merge(dataframe1, dataframe2, on = "employee")
print(dataframe3)

# outer join
dataframe3 = pd.merge(dataframe1, dataframe2, on = "employee", how = "outer")
print(dataframe3)

# left join
dataframe3 = pd.merge(dataframe1, dataframe2, on = "employee", how = "left")
print(dataframe3)

# right join
dataframe3 = pd.merge(dataframe1, dataframe2, on = "employee", how = "right")
print(dataframe3)
