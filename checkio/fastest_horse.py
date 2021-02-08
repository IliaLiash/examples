from collections import Counter
def fastest_horse(horses: list) -> int:
    for element in horses:
        for i in range(len(element)):
            element[i] = int(element[i].split(':')[0]) + int(element[i].split(':')[1])
    res = []
    for element in horses:
        leader = element.index(min(element))
        res.append(leader + 1)
    champ = max(Counter(res), key=Counter(res).get)    
    return champ

if __name__ == '__main__':
    print("Example:")
    print(fastest_horse([['1:13', '1:26', '1:11']]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert fastest_horse([['1:13', '1:26', '1:11'],
                            ['1:10', '1:18', '1:14'],
                            ['1:20', '1:23', '1:15']]) == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")
