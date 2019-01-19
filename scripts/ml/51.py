from sklearn.datasets import load_iris

iris= load_iris()
x= iris.data
y= iris.target

from sklearn.linear_model import LogisticRegression
logreg= LogisticRegression()
print(logreg.fit(x, y))
print(logreg.predict(x))

y_pred= logreg.predict(x)
print(len(y_pred))

from sklearn import metrics
print(metrics.accuracy_score(y, y_pred))

from sklearn.neighbors import KNeighborsClassifier
knn= KNeighborsClassifier(n_neighbors= 5)
print(knn.fit(x, y))

print(x.shape)
print(y.shape)

from sklearn.model_selection import train_test_split
print(x.shape)
print(y.shape)

x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.4,
        random_state= 4)
print(x_test.shape)
print(x_train.shape)
print(y_test.shape)
print(y_train.shape)

logreg= LogisticRegression()
logreg.fit(x_train, y_train)
y_pred= knn.predict(x_test)
print(metrics.accuracy_score(y_test, y_pred))

k_range= range(1, 26)
scores= []
for k in k_range:
    knn= KNeighborsClassifier(n_neighbors= k)
    knn.fit(x_train, y_train)
    y_pred= knn.predict(x_test)
    scores.append(metrics.accuracy_score(y_test, y_pred))
print(scores)

import matplotlib.pyplot as plt
plt.plot(k_range, scores)

plt.xlabel('k for kNN')
plt.ylabel('Testing Accuracy')

plt.show()
