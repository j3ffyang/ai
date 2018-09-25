# Logistic Regression

from sklearn.linear_model import LogisticRegression
from urllib.request import urlopen
from sklearn.datasets import load_iris

lines = urlopen("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
lines = map(lambda s: s.strip(), lines)

iris = load_iris()

X = iris.data
y = iris.target

from sklearn.neighbors import KNeighborsClassifier
knn  = KNeighborsClassifier(n_neighbors=1)
knn5 = KNeighborsClassifier(n_neighbors=5)
knn8 = KNeighborsClassifier(n_neighbors=8)
knn.fit(X,y)
knn5.fit(X,y)
knn8.fit(X,y)

logisticreg = LogisticRegression()
print(logisticreg.fit(X,y))

prediction = knn.predict([[5.1, 3.5, 1.4, 0.2], [6.3, 3.3, 4.7, 1.6]])
print(prediction)

prediction5 = knn5.predict([[5.1, 3.5, 1.4, 0.2], [6.3, 3.3, 4.7, 1.6]])
print(prediction5)

prediction_lr = logisticreg.predict([[5.1, 3.5, 1.4, 0.2], [6.3, 3.3, 4.7, 1.6]])
print(prediction_lr)
