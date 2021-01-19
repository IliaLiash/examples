def create_intervals(data):
    if len(data) == 0:
        return []
    elif len(data) == 1:
        list_1 = sorted(list(data))
        tuple_1 = (list_1[0], list_1[-1])
        return list([tuple_1])        
        
    list_1 = sorted(list(data))
    buffer = [list_1[0]]
    result = []
    
    for i in range(len(list_1)-1):        
        if list_1[i+1] - list_1[i] <= 1:
            buffer.append(list_1[i+1])
            if len(buffer) == len(list_1):
                result.append(tuple(list([buffer[0], buffer[-1]])))
        else:
            result.append(tuple(list([buffer[0], buffer[-1]])))
            buffer = [list_1[i+1]]
    
    if len(buffer) >= 1 and buffer[0] != result[0][0]:
        result.append(tuple(list([buffer[0], buffer[-1]])))        
    
    return result