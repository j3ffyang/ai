import pandas as pd

cereal_df = pd.read_csv("./cereal.csv")
print(cereal_df.head())

print(cereal_df['calories'].dtypes)
print(cereal_df['fiber'].dtypes)
print(cereal_df['fat'].dtypes)

print(cereal_df)
