def mymap(func, *args):
    return list(map(func, *args))

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

print(mymap(lambda x, y: x + y, numbers1, numbers2))

print(mymap(str.upper, ['a', 'b', 'c', 'd', 'e']))

print(mymap(lambda x: x**2, [1, 2, 3, 4, 5]))
