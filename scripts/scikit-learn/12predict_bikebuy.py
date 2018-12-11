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

test_size= .30
seed= 45


