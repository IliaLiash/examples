#character_count("asdfaa") == {"a":3, "s":1, "d":1, "f":1}

def character_count(s):
    d = {}
    set_string = set(s)
    for element in set_string:
        d[element] = s.count(element)
        
    return d        
   
print(character_count("asdfaa"))