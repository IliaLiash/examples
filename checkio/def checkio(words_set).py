def checkio(words_set):
    flag = False
    for element1 in words_set:
        for element2 in words_set:
            if (element1.endswith(element2) or element2.endswith(element1)) and element1 != element2:
                flag = True
                break
            
    return flag