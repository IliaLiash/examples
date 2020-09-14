n, d = int(input()), {}

for i in range(n):
    k, v = input().split()   
    if k not in d.keys():
        d[k] = [int(v)]
    elif k in d.keys():
        d[k].append(int(v))

for k, v in sorted(d.items()):
    d[k] = sum(v)
    print(k, d[k])