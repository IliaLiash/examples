def steps_to_convert(line1, line2):
    count = 0
    if line1 in line2 or (line1 == '' or line2 == ''):
        len_1 = len(line1)
        len_2 = len(line2)
        return abs(max(len_1,len_2) - min(len_1,len_2))
    for i in range(len(line2)):
        try:
            if line1[i] == line2[i]:
                continue
            else:
                count += 1
        except IndexError:
            count += 1
    return count
    

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert steps_to_convert('line1', 'line1') == 0, "eq"
    assert steps_to_convert('line1', 'line2') == 1, "2"
    assert steps_to_convert('line', 'line2') == 1, "none to 2"
    assert steps_to_convert('ine', 'line2') == 2, "need two more"
    assert steps_to_convert('line1', '1enil') == 4, "everything is opposite"
    assert steps_to_convert('', '') == 0, "two empty"
    assert steps_to_convert('l', '') == 1, "one side"
    assert steps_to_convert('', 'l') == 1, "another side"
    print("You are good to go!")
