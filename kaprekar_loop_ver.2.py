def numerics(n):
    list1 = []
    
    while n != 0:
        list1.append(n % 10)
        n = n // 10
    
    return list1

def kaprekar_step(L):
    L = sorted(L)
    
    num1 = ''.join(str(element) for element in L)
    num2 = ''.join(str(element) for element in L[::-1])
    
    return int(num2) - int(num1)

def kaprekar_loop(n):
    list1 = []
   
    if n in [100, 1000, 100000]:
        return print("Ошибка! На вход подано число {}, не удовлетворяющее условиям процесса Капрекара".format(n))
    if len(set(str(n))) == 1:
        return print("Ошибка! На вход подано число {}, не удовлетворяющее условиям процесса Капрекара".format(n))
    
    while n not in [495, 6174, 549945, 631764]:
        
        if n in list1:
            print("Следующее число - {}, кажется процесс зациклился...".format(n))
            break
        else: 
            print(n)
            list1.append(n)
            n = kaprekar_step(numerics(n))
        
    if n in [495, 6174, 549945, 631764]:
        print(n)