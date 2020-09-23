import numpy as np

n, m = map(int, input().split())
k = int(input())

A = np.arange(k, k+m)

Z = np.zeros((n,m))

Z += A