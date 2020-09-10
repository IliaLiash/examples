from datetime import*

y,m,d = [int(i) for i in input().split()]
n = int(input())

d2 = str(date(y,m,d) + timedelta(n)).split('-')

for i in range(len(d2)):
    if d2[i].startswith('0'):
        d2[i] = d2[i].replace('0','')

print(*d2)