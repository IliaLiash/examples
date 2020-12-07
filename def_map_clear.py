digits = ["12", "145", "  45", "12.4", "45,14", "15 645"]

def clear(i):    
    i = float(i.replace(',','.').replace(' ',''))
    return i

right_digits = map(clear, digits)