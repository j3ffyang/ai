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

# url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
url= 'iris.csv'
names= ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset= pandas.read_csv(url, names= names)

print(dataset.shape)
