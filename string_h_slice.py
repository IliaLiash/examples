s = input()
a = s.find('h')
b = s.rfind('h')

print(s[:a + 1] + s[a + 1:b].replace('h','H') + s[b:])
