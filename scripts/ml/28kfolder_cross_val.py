# https://www.udemy.com/introduction-to-data-science-using-python/learn/v4/t/lecture/9387386?start=1193

from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier

iris= load_iris()
X, y= iris.data, iris.target

knn= KNeighborsClassifier(n_neighbors= 5)
scores= cross_val_score(knn, X, y, cv= 10, scoring= 'accuracy')
print(scores.mean())

