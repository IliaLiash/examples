from math import*

def derivative(f, x0=0):
    dx = 0.000001
    return round((f(x0 + dx) - f(x0)) / dx,3)