# https://www.udemy.com/introduction-to-data-science-using-python/learn/v4/t/lecture/9387376?start=1420

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

import warnings 
warnings.filterwarnings("ignore", category= FutureWarning)

iris= load_iris()
X= iris.data 
y= iris.target

# X_train, X_test, y_train, y_test= train_test_split(X, y, test_size= 0.3)
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size= 0.4, random_state= 4)

print(X.shape)
print(X_train.shape)
print(X_test.shape)

# predict by logisticregression
from sklearn import metrics 

logreg= LogisticRegression()
logreg.fit(X_train, y_train)
y_pred= logreg.predict(X_test)
print(metrics.accuracy_score(y_test, y_pred))

# predict by kNN
from sklearn.neighbors import KNeighborsClassifier
knn= KNeighborsClassifier(n_neighbors= 1)
knn.fit(X_train, y_train)
y_pred= knn.predict(X_test)
print(metrics.accuracy_score(y_test, y_pred))

knn5= KNeighborsClassifier(n_neighbors= 5)
knn5.fit(X_train, y_train)
y_pred= knn5.predict(X_test)
print(metrics.accuracy_score(y_test, y_pred))
