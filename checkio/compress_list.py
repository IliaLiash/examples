from typing import Iterable

def compress(items: list) -> Iterable:
    if len(items) == 0:
        return items
        
    list_1 = [items[0]]
    for i in range(1, len(items)):
        if items[i-1] != items[i]:
            list_1.append(items[i])
    
    return list_1