import pandas as pd

csv_path='https://ibm.box.com/shared/static/keo2qz0bvh4iu6gf5qjq4vdrkt67bvvb.csv'
df = pd.read_csv(csv_path)

df.head()

xlsx_path='https://ibm.box.com/shared/static/mzd4exo31la6m7neva2w45dstxfg5s86.xlsx'
df1 = pd.read_excel(xlsx_path)
df1.head()
x=df1[['Length']]
