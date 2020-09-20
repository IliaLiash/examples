import re


f1 = open(sheet)
f2 = open(mean)

text1 = f1.read()
text2 = f2.read()

nums = list(map(int, re.findall(r'\s[1-5]\s', text1)))
average = (sum(nums) / len(nums))


if average == int(text2):
    print('OK')
else:
    print('ERROR')