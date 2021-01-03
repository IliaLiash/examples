original_tags = [" python", "SQL", " PHP "]

# После выполнения кода в переменной tags будет список ["python", "sql", "php"]

def maps(*args):
    tags = args[-1]
    for i in range(len(args)-1):
        tags = list(map(args[i],tags))
    return tags