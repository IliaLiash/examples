import numpy as np

def encode(a):
    a = np.append(a,0)
    b = []
    c = []
    
    for i in range(len(a)-1):
        if a[i] != a[i+1]:
            b.append(a[i])
    
    count = 1
    
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            count += 1
        elif a[i] != a[i+1]:
            c.append(count)
            count = 1
 
    return np.array(b), np.array(c)

X = np.array([1, 2, 2, 3, 3, 1, 1, 5, 5, 2, 3, 3])
print(encode(X))