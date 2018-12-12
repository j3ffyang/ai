# https://www.udemy.com/a-gentle-introduction-to-machine-learning-using-scikit-learn/learn/v4/t/lecture/6790082?start=0

from pandas import read_csv
from numpy import set_printoptions
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

filename= 'BBC.csv'
dataframe= read_csv(filename)
array= dataframe.values

# create array
X= array[:, 0:11]
Y= array[:, 11]

# accuracy
print(dataframe.groupby('BikeBuyer').size())

test_size= 0.25 
seed= 7

X_train, X_test, Y_train, Y_test= train_test_split(X, Y, test_size= test_size, random_state= seed)

model= SVC()
model.fit(X_train, Y_train)

result= model.score(X_test, Y_test)

print(("Accuracy: %.3f%%") % (result* 100.0))
