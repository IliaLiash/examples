import numpy as np
from scipy import linalg

X = np.array([[1, 60],
             [1, 50],
             [1, 75]])

y = np.array([[10],
             [7],
             [12]])

step1 = X.T.dot(X)
step2 = linalg.inv(step1)
step3 = step2.dot(X.T)
b = step3.dot(y)

print(b)