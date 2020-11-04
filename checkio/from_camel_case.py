def from_camel_case(name):
    
    for symbol in name:
        if symbol.isupper():
            name = name.replace(symbol, '_' + symbol.lower())
            
    if name[0] == '_':
        name = name[1:]
        
    return name