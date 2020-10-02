'''
Дан текст: в первой строке записано количество строк в тексте, а затем сами строки. Выведите все слова, встречающиеся в тексте, по одному на каждую строку.
Слова должны быть отсортированы по убыванию их количества появления в тексте, а при одинаковой частоте появления — в лексикографическом порядке.
'''

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
