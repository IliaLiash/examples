#Напишите программу, которая выводит слово, которое встречается в тексте наибольшее число раз.

n = int(input())
list1 = []
d = {}

for _ in range(n):
    list1.extend(input().split())

for element in list1:
    d[element] = list1.count(element)
    
for k, v in d.items():
    if v == max(d.values()):
        print(k)