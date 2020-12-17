def follow(instructions):
    res = [0,0]
    for element in instructions:
        if element == 'f':
            res[1] += 1
        elif element == 'b':
            res[1] -= 1
        elif element == 'l':
            res[0] -= 1
        elif element == 'r':
            res[0] += 1
    return tuple(res)


if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")
