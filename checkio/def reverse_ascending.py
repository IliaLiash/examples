def reverse_ascending(items):
    
    if len(items) == 0 or len(items) == 1:
        return items
        
    list_1 = [items[0]]
    res = []
  
    for i in range(1,len(items)):    
                    
        if  items[i] > items[i-1]:
            list_1.append(items[i])
            if i == len(items) - 1:
                res.extend(sorted(list_1)[::-1])
                    
        if items[i] <= items[i-1]:
            res.extend(sorted(list_1)[::-1])
            list_1 = [items[i]]
            if i == len(items) - 1:
                res.extend(sorted(list_1)[::-1])       
            
    return res