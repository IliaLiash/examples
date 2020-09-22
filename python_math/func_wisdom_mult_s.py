def multiplication_check_list(start=10, stop=99, length_check = True):
      
    count1 = 0
    count2 = 0
    
    for i in range(start, stop + 1):
        for k in range(start, stop + 1):
                   
            a = 100 - i
            b = 100 - k
            c = 100 - a - b
            d = a * b
            
            
            if length_check == True:
                if len(str(d)) == 1:
                    num = int(str(c) + '0' + str(d))
                else:
                    num = int(str(c) + str(d)) 
            else:
                num = int(str(c) + str(d))
            
            if num == i*k:
                count1 += 1
            else:
                count2 += 1
                
    print('Правильных результатов:', count1)
    print('Неправильных результатов:', count2)
    
'''
Напишите 2 функцию multiplication_check_list(start=10, stop=99, length_check = True)

Для проверки всех пар в интервале.

В зависимости от значения аргумента length_check добавляйте при необходимости 0 при конкатенации.

 

multiplication_check_list должна уметь печатать:

Правильных результатов: n
Неправильных результатов: m
Примечание. Пары, где числа поменялись местами считаются РАЗНЫМИ.

Например, в интервале от 11 до 12 есть 4 пары:

11х11, 11х12, 12х11, 12х12

 

Рекомендуется использовать ранее написанные функции и реализовать вспомогательную функцию multiplication_check(x, y, length_check = True).

Примечание. В этой задаче не нужно ничего считывать и ничего выводить на печать. Только реализовать функцию. 
'''