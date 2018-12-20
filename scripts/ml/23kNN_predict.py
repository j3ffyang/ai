
from sklearn.datasets import load_iris

iris= load_iris()
# print(type(iris))
print(iris.data)

print(iris.feature_names)   # col name
print(iris.target_names)    # prediction col

print(iris.target)          # the prediction = target 

print(type(iris.data))
print(type(iris.target))

X= iris.data    # all data without prediction 
y= iris.target  # prediction datasets

from sklearn.neighbors import KNeighborsClassifier
knn= KNeighborsClassifier(n_neighbors= 1)

print(knn)

knn.fit(X, y)

# prediction= knn.predict([[2, 4, 3, 1]])
prediction= knn.predict([[2, 4, 3, 1], [4, 6, 5, 3]])
print(type(prediction))
print(prediction)

print(iris.target_names[0])
print(iris.target_names)

from sklearn.neighbors import KNeighborsClassifier
knn5 = KNeighborsClassifier(n_neighbors= 5)
knn5.fit(X, y)
prediction5= knn5.predict([[2, 4, 3, 1], [4, 6, 5, 3]])
print(prediction5)

from sklearn.neighbors import KNeighborsClassifier
knn8 = KNeighborsClassifier(n_neighbors= 8)
knn8.fit(X, y)
prediction8= knn8.predict([[2, 4, 3, 1], [4, 6, 5, 3]])
print(prediction8)
