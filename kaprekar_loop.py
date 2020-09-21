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
    while n != 6174:
        print(n)
        n = kaprekar_step(numerics(n))
    print(n)