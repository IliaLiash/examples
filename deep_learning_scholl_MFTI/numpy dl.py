import numpy as np
'''
a = np.array([1, 2, 3, 7])
print(type(a))
print(a.size)

b = np.linspace(10, 32, 12)
print(b)

list1 = [1, 2, 3, 5, 10]
list2 = list1[0:3]
list2[0] += 1000

print(list1)
print(list2)


a = np.linspace(-4*np.pi, 4*np.pi,100)

for i in range(len(a)):
    print(np.sin(i)**2 + np.cos(i)**2, end=' ')

print()
print(np.all(a))
'''
'''
a = -1*np.eye(8)[::-1] + np.diag(np.arange(3, 25, 3))

print(a)
'''

is_prime = np.ones(100)
is_prime[:2] = 0

print(is_prime)
