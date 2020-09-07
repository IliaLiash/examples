#вывести номер этой строки  и номер символа, с которого начинается первое вхождение этой подстроки
'''
n = int(input())
list1 = []

for i in range(n):
    i = input().lower()
    list1.append(i)

for i in range(len(list1)):
    if 'рок' in list1[i]:
        print(i+1, list1[i].rfind('рок')+1)
'''

#Salt
'''
n = int(input())
list_1 = []

for i in range(n):
    s = input().lower()
    if 'соль' in s:
        continue
    else:
        list_1.append(s)

print(*list_1, sep=', ')
'''

s = input().lower()

print(max([s.count(i) for i in s]))