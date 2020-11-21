def how_deep(structure):
    
    k = 0
    s = ''
    
    for element in str(structure):
        if element == '(' or element == ')':
            s += element
            
    for i in range(1,int(len(s)/2)+1):
        if s[i-1] == '(' and s[-i] == ')':
            k += 1
        elif s[i-1] == s[-i]:
            k += 1
            break
        elif s[i-1] != s[-i]:
            break
    return k
