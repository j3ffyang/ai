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
print(scores.mean())

k_range = range(1, 45)
k_scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors= k)
    scores = cross_val_score(knn, X, y, cv= 10, scoring='accuracy')
    k_scores.append(scores.mean())

print(k_scores)

import matplotlib.pyplot as plt
# matplotlib inline
plt.plot(k_range, k_scores)
plt.xlabel('K value for KNN algorithm')
plt.ylabel('Mean accuracy scores')

# we can see when x= 12/ 18/ 20, y is highest
plt.show()
