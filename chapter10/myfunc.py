#take any number of arguments, zero or more
def myfunc(*args):
    for a in args:
        print(a, end=' ')
    if args:
        print()

#take keyword arguments, dicts
def myfunc2(**kwargs):
    for k, v in kwargs.items():
        print(k, v, sep='->', end=' ')
    if kwargs:
        print()

#take any number and type of arguments
def myfunc3(*args, **kwargs):
    if args:
        for a in args:
            print(a, end=' ')
        print()
    if kwargs:
        for k,v in kwargs.items():
            print(k, v, sep='->', end=' ')
        print()