#3ab4c2CaB  ---  aaabccccCCaB
string = input()
n, new_string = str(), str()
       
for i in range(len(string)):
    if string[i].isdigit() == True and string.isdigit() == False:   #Считываем цифры, если вся строка сама не число
        n += string[i]                                              #Записываем цифры в строку
        if string[i].isdigit() == True and string[i + 1].isalpha() == True: #Если после цифры идет буква...
            new_string += int(n) * string[i + 1]                            #Добавляем накопленную int(строку) * на букву
            n = str()                                                       #Очищаем строку
    elif string[i].isalpha() == True and string[i - 1].isdigit() == False:  #Если перед буквой тоже буква - добавляем
        new_string += string[i]
            
print(new_string)
