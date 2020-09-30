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