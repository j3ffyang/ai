# https://data-flair.training/blogs/python-ml-data-preprocessing/#

import pandas, scipy, numpy
from sklearn.preprocessing import LabelEncoder

df= pandas.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv', sep= ';')

array= df.values

# separating data into input and output components
x= array[:, 0:8]
y= array[:, 8]

label_encoder= LabelEncoder()
input_classes= ['Havells', 'Philips', 'Syska', 'Eveready', 'Lloyd']
label_encoder.fit(input_classes)

for i, item in enumerate(label_encoder.classes_):
    print(item, '-->', i)
