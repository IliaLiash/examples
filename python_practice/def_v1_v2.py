import numpy as np

def vector_sum(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)
    
    return v1 + v2

v1 = (1, 5)
v2 = (2, 3)

print(tuple(vector_sum(v1, v2)))