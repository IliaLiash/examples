n = int(input())
d = dict([input().split() for i in range(n)])
    
s_find = input()

for k, v in d.items():
    if d[k] == s_find:
        print(k)
    elif s_find in d.keys() and d[s_find] == v:
        print(v)