def verify_anagrams(a, b):
    a = a.replace(' ','')
    b = b.replace(' ','')
    a = ''.join(sorted(a.lower()))
    b = ''.join(sorted(b.lower()))
    
    return a == b