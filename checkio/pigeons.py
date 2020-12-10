def checkio(number):
    
    minute = 0
    fed_pigeons = 0
    pigeons = 0
    
    while True:
        minute += 1
        old_pigeons = pigeons
        pigeons += minute
        if number < pigeons:
            remains_food = number - old_pigeons
            if remains_food > 0:
                fed_pigeons += remains_food
            break
        number -= pigeons
        fed_pigeons += minute
            
    return fed_pigeons

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"