n = int(input())
text = ''
for i in range(n):
    text += input()
    
for element in text:
    if element in ".,!?:;":
        text = text.replace(element,' ')
    
text = text.lower()

count_max = 0

for element in text:
    if text.count(element) > count_max:
        count_max = text.count(element)
        find = element
        
print(count_max, element)