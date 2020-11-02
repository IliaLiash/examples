def days_diff(a, b):
    
    one = datetime(a[0], a[1], a[2]) 
    two = datetime(b[0], b[1], b[2]) 
    
    return abs((one - two).days)