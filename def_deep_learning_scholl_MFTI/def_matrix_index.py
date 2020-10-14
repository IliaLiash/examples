import numpy as np

def transform(X, a=1):

    B = np.copy(X)          #создаем копию X
    for string in B:
        for i in range(len(string)):        #проходим по строкам, меняя элементы по условию
            
            if i % 2 == 0:
                string[i] = string[i]**3            
            
            elif i % 2 != 0:
                string[i] = a
    
    B = B[:, ::-1]                          #разворачиваем матрицу
    
    return np.concatenate((X, B), axis=1)   #склеиваем полученную матрицу с изначальной

M = np.array([[100,200,300,400,500]])

print(transform(M))