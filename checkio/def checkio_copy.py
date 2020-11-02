def checkio(data: list) -> list:
    
    list_1 = data.copy()
    for element in data:
        if data.count(element) == 1:
            list_1.remove(element)

    return list_1