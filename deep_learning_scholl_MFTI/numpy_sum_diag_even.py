import numpy as np #не стирать!        

def diag_2k(a):
    total = 0
    a = a.reshape(len(a)**2)
    for i in range(0, len(a), int(len(a)**0.5)+1): 
        if a[i] % 2 == 0:
            total += a[i]

    return total

M = np.array([[2, 0, 0],
              [0, 2, 4],
              [0, 0, 1]])

print(diag_2k(M))
