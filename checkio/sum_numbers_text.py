def sum_numbers(text: str) -> int:
    res = 0
    list_1 = text.split()
    
    for element in list_1:
        if element.isdigit():
            res += int(element)
    
    return res