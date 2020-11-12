def checkio(line: str) -> str:
    str_a = 'aeiouy'
    str_b = 'bcdfghjklmnpqrstvwxz'
    
    list_1 = line.replace('.',' ').replace(',', ' ').lower().split()
    count = len(list_1)        
    
    for word in list_1:
        if word.isdigit():
            count -= 1           
        elif len(word) > 1:
            
            for i in range(1, len(word)):             
                if word[i].isdigit() or word[i-1].isdigit():
                    count -= 1
                    break
                elif ((word[i] in str_a) and (word[i-1] in str_a)) or  ((word[i] in str_b) and (word[i-1] in str_b)):
                    count -= 1
                    break
                
        elif len(word) == 1:
            count -= 1    

    return count