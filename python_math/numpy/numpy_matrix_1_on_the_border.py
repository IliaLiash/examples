import numpy as np

n, m = map(int, input().split())

Z = np.zeros((n,m))

Z[0] = 1
Z[:,0] = 1
Z[:,m - 1] = 1
Z[n - 1] = 1