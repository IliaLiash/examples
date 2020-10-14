import numpy as np

x_shape = tuple(map(int, input().split()))
X = np.fromiter(map(int, input().split()), np.int).reshape(x_shape)
y_shape = tuple(map(int, input().split()))
Y = np.fromiter(map(int, input().split()), np.int).reshape(y_shape)

if x_shape[1] == Y.T.shape[0]:
    prod = X.dot(Y.T)
    print(prod)
else:
    print('matrix shapes do not match')
