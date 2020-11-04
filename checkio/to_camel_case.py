def to_camel_case(name):
    
    if name[0].islower():
        name = name.replace(name[0], name[0].upper(),1)
    
    for i in range(len(name)-name.count('_')):
        if name[i] == '_':
            name = name.replace(name[i]+name[i+1], name[i+1].upper())