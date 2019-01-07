from sklearn.datasets import load_iris

import warnings
warnings.filterwarnings("ignore", category= FutureWarning)

iris= load_iris()
# print(iris.data)

print(iris.feature_names)   # all col names
print(iris.target_names)    # 3 predicted species in prediction col
print(iris.target)          # the prediction = target 

X= iris.data    # all data without prediction 
y= iris.target  # prediction datasets

from sklearn.linear_model import LogisticRegression
logreg= LogisticRegression() 
# logreg= LogisticRegression(solver= 'lbfgs') # add 'solver' to get rid of warning 
logreg.fit(X, y)
print(logreg.fit(X, y))

prediction= logreg.predict([[2,4,3,1],[4,6,5,3]])
print(prediction)
