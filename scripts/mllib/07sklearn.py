from sklearn import datasets
from sklearn import metrics
from sklearn.svm import SVC

# load the iris datasets
ds= datasets.load_iris()
model= SVC()

# fit an SVM model to the data 
model.fit(ds.data, ds.target)

print(model)

# make predictions
expected= ds.target
predicted= model.predict(ds.data)

# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
