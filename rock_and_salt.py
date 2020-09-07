#Number of string and symbol, from which first occurrence of this substring begins
'''
n = int(input())
list1 = []

for i in range(n):
    i = input().lower()
    list1.append(i)

for i in range(len(list1)):
    if 'rock' in list1[i]:
        print(i+1, list1[i].rfind('rock')+1)
'''

#Salt
'''
n = int(input())
list_1 = []

for i in range(n):
    s = input().lower()
    if 'salt' in s:
        continue
    else:
        list_1.append(s)

print(*list_1, sep=', ')
'''

s = input().lower()
