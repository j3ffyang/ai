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
# use ravel() to correct shape challenge

from sklearn.metrics import accuracy_score
result= accuracy_score(Y_test, knn.predict(X_test[['ApplicantIncome', 
    'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 
    'Credit_History']]))

# print(result)
print(("Accuracy: %.3f%%") % (result* 100.0))

print('Loan_Status in train dataset. In result, 70% of approved loans')
print(Y_train.Target.value_counts()/ Y_train.Target.count()) 

print('Use the above train dataset to predict for "test"')
print(Y_test.Target.value_counts()/ Y_test.Target.count())
