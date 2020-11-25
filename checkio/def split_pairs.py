def split_pairs(a):
    if len(a) % 2 != 0:
        a += '_'
    
    list1= []
    k = 2
    
    if len(a) % 2 == 0:
        for i in range(0, len(a)+1, 2):
            if a != '':
                list1.append(a[:k])
                a = a[k:]
                
    return list1