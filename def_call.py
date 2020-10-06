'''
Напишите функцию call, которая будет принимать произвольную функцию, аргументы для неё и делать вызов переданной функции.
'''


def call(fun,*args,**kwargs):
    if len(kwargs) != 0:
        return fun(*args,**kwargs)
    else:
        return fun(*args)