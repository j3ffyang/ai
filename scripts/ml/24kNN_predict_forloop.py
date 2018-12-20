# https://www.udemy.com/introduction-to-data-science-using-python/learn/v4/content

from sklearn.datasets import load_iris

iris= load_iris()
print(iris.data)

print(iris.feature_names)   # col name as 4 specs of data 
print(iris.target_names)    # 3 predicted species in prediction col
print(iris.target)          # the actual prediction = target 

X= iris.data    # all data without prediction 
y= iris.target  # prediction datasets

from sklearn.neighbors import KNeighborsClassifier

for i in range(1, 31):  # usually n_neighbors=1, 5, 8 in practice
    knn= KNeighborsClassifier(n_neighbors= i)
    print(knn)
    knn.fit(X, y)
    prediction= knn.predict([[2, 4, 3, 1], [4, 6, 5, 3]])
    print(prediction)
