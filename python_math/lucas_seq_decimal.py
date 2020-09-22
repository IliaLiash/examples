def fi(L0, L1, n):
    for __ in range(n - 1):
        L0, L1 = L1, L0 + L1
    return Decimal(L1) / Decimal(L0)