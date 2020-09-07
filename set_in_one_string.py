#Дан список чисел. Определите, сколько в нем встречается различных чисел.
'''
print(len(set([int(i) for i in input().split()])))
'''

#Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.
'''
print(*set([int(i) for i in input().split()]).intersection(set([int(i) for i in input().split()])))
'''
#Все числа, которые входят как в первый, так и во второй список и выведите их в порядке возрастания.
'''
print(*set(sorted([int(i) for i in input().split()])).intersection(set(sorted([int(i) for i in input().split()]))))
'''

#YES, если это число ранее встречалось в последовательности или NO, если не встречалось.
'''
a = [int(i) for i in input().split()]
b = []

for element in a:
    if element not in b:
        b.append(element)
        print('NO')
    else:
        print('YES')
'''

#Сколько слов в тексте
'''
n = int(input())
a = []
count = 0

for _ in range(n):
    s = input().split()
    a.extend(s)

print(len(set(a)))
'''


