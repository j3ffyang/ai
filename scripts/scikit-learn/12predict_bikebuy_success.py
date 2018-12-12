# https://www.udemy.com/a-gentle-introduction-to-machine-learning-using-scikit-learn/learn/v4/t/lecture/6759088?start=0

from pandas import read_csv
from numpy import set_printoptions 
from sklearn.model_selection import train_test_split 
from sklearn.svm import SVC 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.ensemble import RandomForestClassifier 

filename= "BBC.csv"
dataframe= read_csv(filename) 

array= dataframe.values
X= array[:, 0:11]
Y= array[:, 11]

# print(X)
# print(Y)

test_size= .30
seed= 45

X_train, X_test, Y_train, Y_test= train_test_split(X, Y, test_size=test_size, random_state=seed)

model= RandomForestClassifier()
model.fit(X_train, Y_train)
 
result= model.score(X_test, Y_test)

print(("Accuracy: %.3f%%") % (result* 100.0))
