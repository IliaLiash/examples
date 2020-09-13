s = input().split()
i = 0

for element in s:
    print(s[:i].count(element), end=' ')
    i += 1
