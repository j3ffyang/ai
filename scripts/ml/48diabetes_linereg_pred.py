# https://data-flair.training/blogs/machine-learning-algorithms-in-python/

import matplotlib.pyplot as plt 
import numpy as np 
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error,r2_score

diabetes= datasets.load_diabetes()
diabetes_x= diabetes.data[:, np.newaxis, 2]
diabetes_x_train= diabetes_x[: -30] # splitting data into train and test
diabetes_x_test= diabetes_x[-30 :]
diabetes_y_train= diabetes.target[: -30] # split targets into train & test
diabetes_y_test= diabetes.target[-30 :]
regr= linear_model.LinearRegression()    # linear regression obj
regr.fit(diabetes_x_train, diabetes_y_train)

diabetes_y_pred= regr.predict(diabetes_x_test)  # make prediction
print(regr.coef_)

print(mean_squared_error(diabetes_y_test, diabetes_y_pred))    

print(r2_score(diabetes_y_test, diabetes_y_pred))   # variance score

plt.scatter(diabetes_x_test, diabetes_y_test, color= 'lavender')
plt.plot(diabetes_x_test, diabetes_y_pred, color= 'pink', linewidth= 3)
plt.show()
