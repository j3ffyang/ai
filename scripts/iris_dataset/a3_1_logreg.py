# Logistic Regression

from sklearn.linear_model import LogisticRegression
from urllib.request import urlopen
from sklearn.datasets import load_iris

lines = urlopen("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
lines = map(lambda s: s.strip(), lines)

iris = load_iris()

X = iris.data
y = iris.target

logisticreg = LogisticRegression()
print(logisticreg.fit(X,y))

prediction_lr = logisticreg.predict([[2,4,3,1], [4,6,5,3]])
print(prediction_lr)

print(iris.target_names)
