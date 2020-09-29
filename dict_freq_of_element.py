#Посчитать для каждого имени количество его повторений и вывести на печать
n = int(input())
d = {}
list1 = []
for i in range(n):
    name = input()
    list1.append(name)
    d[name] = list1.count(name)
    
for key in sorted(d):
    print(key,': ', d[key], sep='')