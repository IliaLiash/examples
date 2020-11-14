def yaml(a):
    d = {}
    list_1 = a.split('\n')
    for element in list_1:
        if element == '':
            continue
        elif element.split(':')[1].strip().isdigit():
            d[element.split(':')[0].strip()] = int(element.split(':')[1].strip())
        else:
            d[element.split(':')[0].strip()] = element.split(':')[1].strip()    
    
    return d