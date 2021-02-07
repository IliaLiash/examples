def non_repeat(line):
    if len(set(line)) == len(line):
        return line        
    i = 1
    k = 1               #for nested strings - repeat from begin (from k and not from current i)
    res = []
    s = line[0]
    while i < len(line):
        if line[i] not in s:
            s += line[i]
            i += 1
            if i == len(line):
                res.append(s)
        else:
            res.append(s)
            s = line[k]
            k += 1
            i = k
    return sorted(res, key=lambda x: -len(x))[0]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert non_repeat('aaaaa') == 'a', "First"
    assert non_repeat('abdjwawk') == 'abdjw', "Second"
    assert non_repeat('abcabcffab') == 'abcf', "Third"
    print('"Run" is good. How is "Check"?')
