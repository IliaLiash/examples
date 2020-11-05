'''
Вводится количество строк словаря затем вводятся сами строки, в формате <название> - <определение>, каждая на отдельной строке.
Затем вводится количество определений которые надо вернуть и сами определения, каждое на отдельной строке.
Выводится строка в формате <название> - <определение> или выводится "Нет определения", если его нет в словаре.
'''

n = int(input())
d = {}

for _ in range(n):
    list1 = input().split(' ',1)
    d[list1[0]] = list1[1]

m = int(input())
list_keys = []

for _ in range(m):
    list_keys.append(input())
    
for element in list_keys:
    if element not in d.keys():
        print('Нет определения')
    else:
        print(element, d[element])