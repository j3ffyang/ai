# Udemy

import numpy as np
from sklearn.model_selection import train_test_split
X, y = np.arange(10).reshape((5, 2)), range(5)

print(X)
print(list(y))
# print(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42)

print(X_train)
print(y_train)
print(X_test)
print(y_test)

print(train_test_split(y, shuffle=False))
