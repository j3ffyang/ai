from urllib.request import urlopen
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier

lines = urlopen("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
lines = map(lambda s: s.strip(), lines)

iris = load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

print(X.shape)
print(X_train.shape)
print(X_test.shape)

print(y_train.shape)
print(y_test.shape)

logisticreg = LogisticRegression()
logisticreg.fit(X_train, y_train)
print(logisticreg)

y_pred = logisticreg.predict(X_test)
print(y_pred)

print(metrics.accuracy_score(y_test, y_pred))

knn  = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print(metrics.accuracy_score(y_test, y_pred))

knn5 = KNeighborsClassifier(n_neighbors=5)
knn5.fit(X_train, y_train)
y_pred = knn5.predict(X_test)
print(metrics.accuracy_score(y_test, y_pred))
