import numpy as np

seed = int(input())
n = int(input())

np.random.seed(seed)

Z = np.random.random_sample(n)
Z = np.sort(Z)