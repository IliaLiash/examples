import numpy as np

n, m = map(int, input().split())
np.random.seed(42)
res = []
Z = np.random.random_sample((n,m))

for i in range(m):
    res.append(np.average(Z[:,i]))

print(min(res))
print(max(res))