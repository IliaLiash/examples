def primes():
    
    
    for i in range(1, 10**6):
        count = 0
        
        for n in range(1,i + 1):
            if i % n == 0:
                count += 1
                
        if count == 2:
            yield i         

y = primes()              
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))