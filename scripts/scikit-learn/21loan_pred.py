# https://www.analyticsvidhya.com/blog/2016/07/practical-guide-data-preprocessing-python-scikit-learn/

import pandas as pd 
import matplotlib.pyplot as plt

X_train= pd.read_csv('loan_pred_X_train.csv')
Y_train= pd.read_csv('loan_pred_Y_train.csv') 

X_test= pd.read_csv('loan_pred_X_test.csv')
Y_test= pd.read_csv('loan_pred_Y_test.csv')

print(X_train.head())

X_train[X_train.dtypes[(X_train.dtypes== "float64") | (X_train.dtypes==" int64")].index.values].hist(figsize=[11, 11])

# plt.show()

from sklearn.neighbors import KNeighborsClassifier
knn= KNeighborsClassifier(n_neighbors= 5)
knn.fit(X_train[['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 
    'Loan_Amount_Term', 'Credit_History']], Y_train.values.ravel())

from sklearn.metrics import accuracy_score
accuracy_score(Y_test, knn.predict(X_test[['ApplicantIncome', 
    'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 
    'Credit_History']]))
