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

from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.4,
        random_state= 4)
print(x_train.shape)
