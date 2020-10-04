def process(sentences):
    list1 = []
    
    for string in sentences:
        s = [i for i in string.split() if i.lower().isalpha()]
        list1.append(s)
    
    for i in range(len(list1)):
        list1[i] = ' '.join(list1[i])
        
    return list1