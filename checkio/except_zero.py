from typing import Iterable

def except_zero(items: list) -> Iterable:
    #создаем копию и сортируем ее
    list_1 = items.copy()
    list_1 = sorted(list_1)
    #удаляем из копии все 0
    while 0 in list_1:
        list_1.remove(0)
    #готовим цикл, где будем добавлять 0 или значение из списка list_1 по порядку. Выбираем подходящую индексацию.   
    res = []
    k = 0
    
    for i in range(len(items)):
        if items[i] == 0:
            res.append(0)
        else:
            res.append(list_1[k])
            k += 1
                        
    return res