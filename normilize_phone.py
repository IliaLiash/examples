from functools import reduce

def normalize_phone(phone):
    return reduce(lambda x,y: x + y, [str(i) for i in phone if i.isdigit()])
