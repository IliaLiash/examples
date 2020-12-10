def long_repeat(line) -> int:
    if len(line) == 0:
        return 0
    else:
        count = 1
        max_len = 1
        line += ' '
    
        for i in range(0,len(line)-1):
            if line[i] == line[i+1]:
                count += 1
            else:
                if count >= max_len:
                    max_len = count
                    count = 1
           
        return max_len

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')