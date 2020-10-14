def max_par(a, b, c):
    if a > 0:
        return None    
    else:
        return -b / (2 *a), -(b**2 - 4*a*c)/(4 * a)

print(max_par(-2, 1, 0))