def letter_queue(commands):
    res = ''
    for i in range(len(commands)):
        if len(commands[i].split()) > 1:
            if commands[i].split()[0] == 'PUSH':
                res += commands[i].split()[1]
        elif commands[i].split()[0] == 'POP' and res != '':
            res = res.replace(res[0],'',1)
        else:
            continue
    return res


if __name__ == '__main__':
    print("Example:")
    print(letter_queue(['PUSH A',
        'POP',
        'POP',
        'PUSH Z',
        'PUSH D',
        'PUSH O',
        'POP',
        'PUSH T']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert letter_queue(['PUSH A',
        'POP',
        'POP',
        'PUSH Z',
        'PUSH D',
        'PUSH O',
        'POP',
        'PUSH T']) == 'DOT'
    assert letter_queue(['POP', 'POP']) == ''
    assert letter_queue(['PUSH H', 'PUSH I']) == 'HI'
    assert letter_queue([]) == ''
    assert letter_queue(["PUSH X","POP","POP","POP","POP","PUSH J","PUSH V","PUSH J","PUSH H","POP","PUSH H","PUSH M","POP","PUSH K","PUSH T"]) == "JHHMKT"
    print("Coding complete? Click 'Check' to earn cool rewards!")