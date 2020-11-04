def checkio(text: str) -> str:

    d = {}
    
    for element in text.lower():
        if element.lower() in d.keys():
            d[element.lower()] += 1
        elif element.isalpha():
            d[element.lower()] = 1
     
    list_1 = [] 
        
    for k,v in d.items():
        if v == max(d.values()):
            list_1.append(k)
            
    return sorted(list_1)[0]