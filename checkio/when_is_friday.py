from datetime import datetime
def friday(day):
    from_date = int(datetime.strptime(day, '%d.%m.%Y').weekday())
    return 4 - from_date if (4 - from_date >= 0) else 1 + from_date

if __name__ == '__main__':
    print("Example:")
    print(friday('23.04.2018'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert friday('23.04.2018') == 4
    assert friday('01.01.1999') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")
