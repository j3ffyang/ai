import pandas as pd 
import matplotlib.pyplot as plt 

df= pd.DataFrame({
    'name':['john', 'lisa', 'peter','carl', 'linda', 'betty'],
    'date_of_birth':['01/21/1988', '03/10/1977', '07/25/1999', '01/22/1977', '09/30/1968', '09/15/1970']
    })

df['date_of_birth']= pd.to_datetime(df['date_of_birth'], infer_datetime_format= True)

plt.clf()
df['date_of_birth'].map(lambda d: d.month).plot(kind= 'hist')
plt.show()

# plt.savefig('output.png')
