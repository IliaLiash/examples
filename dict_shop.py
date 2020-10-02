import sys
d1 = {}

for line in sys.stdin:
    name, *prod = line.split()
    
    if name not in d1.keys():
        d1[name] = [*prod]
    else:
        if prod[0] in d1[name]:
            pos = d1[name].index(prod[0])
            d1[name][pos+1] = int(d1[name][pos+1])
            d1[name][pos+1] += int(prod[1])       
        else:
            d1[name] += prod

for k,v in sorted(d1.items()):
    print(k + ':')
    list2 = []
    for i in range(0,len(v) - 1,2):
        #print(v[i], v[v.index(v[i]) + 1])
        list2.append(str(v[i]) + ' ' + str(v[v.index(v[i]) + 1]))
    print(*sorted(list2), sep='\n')       