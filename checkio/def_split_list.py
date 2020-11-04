from math import ceil
def split_list(items: list) -> list:
    
    list_1 = items[:ceil(len(items)/2)]
    list_2 = items[ceil(len(items)/2):]
    
    return [list_1, list_2]