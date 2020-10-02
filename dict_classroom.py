n = int(input())
d = {}
for i in range(n):
    k, v = input().split()
    if k in d.keys():
        d[k].append(int(v))
    else:
        d[k] = [int(v)]
    
for k,v in sorted(d.items()):
    print(k, round(sum(v) / len(v),1))