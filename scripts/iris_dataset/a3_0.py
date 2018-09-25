# knn from udemy 20180925

from urllib.request import urlopen

lines = urlopen("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
lines = map(lambda s: s.strip(), lines)

for row in lines:
      # print(', '.join(row))
      print(row)

from sklearn.datasets import load_iris
iris = load_iris()

# print(type(iris))
# print(iris.feature_names)
# print(iris.target_names)
# print(iris.target)
# print(iris.data)
# print(type(iris.data))
# print(type(iris.target))

X = iris.data
y = iris.target

from sklearn.neighbors import KNeighborsClassifier
knn  = KNeighborsClassifier(n_neighbors=1)
knn5 = KNeighborsClassifier(n_neighbors=5)
knn8 = KNeighborsClassifier(n_neighbors=8)
# print(knn)
knn.fit(X,y)
knn5.fit(X,y)
knn8.fit(X,y)

# prediction = knn.predict([[2,4,3,1]])
# prediction = knn.predict([[4, 6, 5, 2]])
prediction  = knn.predict([[2,4,3,1], [4,6,5,3]])
prediction5 = knn5.predict([[2,4,3,1], [4,6,5,3]])
prediction8 = knn8.predict([[2,4,3,1], [4,6,5,3]])
print(prediction)
print(prediction5)
print(prediction8)
print(iris.target_names)

