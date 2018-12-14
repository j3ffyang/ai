# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

import pandas
from pandas. plotting import scatter_matrix
import matplotlib.pyplot as plt 
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score 
from sklearn.linear_model import LogisticRegression 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis 
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

from numpy import ndarray

# url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
url= 'iris.csv'
names= ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset= pandas.read_csv(url, names= names)

# dimension of dataset
print(dataset.shape)

# peek at the data 
print(dataset.head(20))

# statistical sum 
print(dataset.describe())

# class distribution 
print(dataset.groupby('class').size())

# create a validation dataset 
# split-out validation dataset 
array= dataset.values
X= array[:, 0:4]
Y= array[:, 4]
validation_size= 0.20 
seed= 7
X_train, X_validation, Y_train, Y_validation= model_selection.train_test_split(X, Y, test_size= validation_size, random_state= seed)

# test options and evaluation metric 
scoring= 'accuracy'

# spot check algorithms 
models= []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))

# evaluate each model in turn 
results= []
names= []
for name, model in models:
    kfold= model_selection.KFold(n_splits= 10, random_state= seed)
    cv_results= model_selection.cross_val_score(model, X_train, Y_train, cv= kfold, scoring= scoring)
    results.append(cv_results)
    names.append(name)
    msg= ("%s: %f (%f)") % (name, cv_results.mean(), cv_results.std())
    print(msg)

# compare algorithms 
fig= plt.figure()
fig.suptitle('Algorithm Comparison')
ax= fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()
