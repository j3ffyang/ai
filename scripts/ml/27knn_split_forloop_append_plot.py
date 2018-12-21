# https://www.udemy.com/introduction-to-data-science-using-python/learn/v4/t/lecture/9387376?start=1420

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris= load_iris()
X, y= iris.data, iris.target

# X_train, X_test, y_train, y_test= train_test_split(X, y, test_size= 0.3)
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size= 0.4, random_state= 4)

# predict by kNN
from sklearn import metrics 
from sklearn.neighbors import KNeighborsClassifier

a, b= [], []
for i in range(1, 31):
    knn= KNeighborsClassifier(n_neighbors= i)
    knn.fit(X_train, y_train)
    y_pred= knn.predict(X_test)
    multi_pred= [i, metrics.accuracy_score(y_test, y_pred)]
    a.append(i)
    b.append(metrics.accuracy_score(y_test, y_pred))

import matplotlib.pyplot as plt 
plt.plot(a, b)
plt.xlabel('n_neighbors value')
plt.ylabel('accuracy_score')
plt.show()
