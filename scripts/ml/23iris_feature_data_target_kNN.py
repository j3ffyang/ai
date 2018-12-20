
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
