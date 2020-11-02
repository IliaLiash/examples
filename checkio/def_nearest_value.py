def nearest_value(values: set, one: int) -> int:
    s = sorted(values)
    min_diff = abs(one - s[0])  #задаем минимальный элемент и разность - как точку начального отсчета
    min_element = s[0]
    
    for element in values:      #в цикле перебираем элементы и сравниваем, как в задачке на больше-меньше
        b = abs(one - element)
        if min_diff > b:
            min_diff = b
            min_element = element  
            
    return min_element

print(nearest_value({4, 7, 10, 11, 12, 17}, 9))