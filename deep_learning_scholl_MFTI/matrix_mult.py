import numpy as np

def no_numpy_mult(first, second):
    raw=[]                              #строка-список
    matrix=[]                           #новая матрица
    
    for i in range(len(first)):
        for j in range(len(second[0])):
            sums=0
            for k in range(len(second)):
                sums = sums + (first[i][k] * second[k][j])  #считаем сумму
            raw.append(sums)                                #добавляем в строку
            
        matrix.append(raw)                                  #добавляем строку к матрице и обнуляем
        raw=[]
         
    return matrix

def numpy_mult(first, second):
    result = np.dot(first, second)
    return result

A = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
B = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8]]

print(no_numpy_mult(A,B))
print(numpy_mult(A,B))
