import numpy as np

def cumsum(A):

    return np.cumsum(A, axis=1)

M = np.array([[2, 0, 0],
              [0, 2, 4],
              [0, 0, 1]])

print(cumsum(M))