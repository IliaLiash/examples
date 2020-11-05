def words_order(text: str, words: list) -> bool:
    list_1 = text.split()
    count = 0
    k = 0
    
    if len(set(words)) != len(words):
        return False
    
    for i in range(len(list_1)):
        try:
            if list_1[i] == words[k]:
                count += 1
                k += 1
        except IndexError:
            continue
    
    if count == len(words):
        return True
    else:
        return False
