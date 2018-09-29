# udemy

from sklearn.datasets import load_iris
iris = load_iris()

X = iris.data
y = iris.target

from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors = 5)
print(knn)

scores = cross_val_score(knn, X, y, cv= 10, scoring='accuracy')
print(scores)
