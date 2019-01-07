# https://data-flair.training/blogs/python-ml-data-preprocessing/#

import pandas, scipy, numpy
from sklearn.preprocessing import OneHotEncoder

df= pandas.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv', sep= ';')

array= df.values

# separating data into input and output components
x= array[:, 0:8]
y= array[:, 8]

encoder= OneHotEncoder()
encoder.fit([[0,1,6,2],
    [1,5,3,5],
    [2,4,2,7],
    [1,0,4,2]
    ])

print(encoder.transform([[2,4,3,4]]).toarray())
