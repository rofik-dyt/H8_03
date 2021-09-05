def add(*args):
    res = 0
    for arg in args:
        res += arg
    return res

def multiply(*args):
    res = 1
    for arg in args:
        res = res * arg
    return res

def divide(*args):
    [res, *sisa] = args
    for arg in sisa:
        res = res / arg
    return res

def kali(*args):
    res = [arg * arg for arg in args]
    return sum(res)
