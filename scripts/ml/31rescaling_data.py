# https://data-flair.training/blogs/python-ml-data-preprocessing/#

# import pandas, scipy, numpy
import pandas
import numpy
from sklearn.preprocessing import MinMaxScaler

df = pandas.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/\
        wine-quality/winequality-red.csv', abssep=';')

array = df.values

# separating data into input and output components
x = array[:, 0:8]
y = array[:, 8]

scaler = MinMaxScaler(feature_range=(0, 1))
rescaledX = scaler.fit_transform(x)
numpy.set_printoptions(precision=3)    # setting precision for output
print(rescaledX[0:5, :])
