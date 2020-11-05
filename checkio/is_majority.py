def is_majority(items: list) -> bool:
    
    if len(items) == 0:
        return False
    
    d = {}
    for element in items:
        d[items.count(element)] = element
        
    a = max(d.keys())

    return d[a]