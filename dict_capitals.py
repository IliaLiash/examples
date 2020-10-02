#Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в какой стране он находится.

n = int(input())
m = {}

for i in range(n):
    country, *cities = input().split()
    
    for city in cities:
        m[city] = country

m = int(input())

for i in range(k):
    city = input()
    print(k[city])
