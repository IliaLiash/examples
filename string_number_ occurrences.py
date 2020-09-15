s = input()
t = input()

count = 0

for i in range(len(s)):
    if t in s[i:len(t) + i]:
        count += 1
        
print(count)