from typing import List, Any

def all_the_same(elements: List[Any]) -> bool:
    flag = True
    
    for i in range(len(elements)-1):
        if elements[i] == elements[i+1]:
            continue
        else:
            return False
            
    return True