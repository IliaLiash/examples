def luka(L0, L1, n):
    a = L0
    b = L1
    for _ in range(n):
        a, b = b, a + b
    return a