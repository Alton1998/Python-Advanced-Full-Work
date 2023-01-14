# Decorators

# Everything in python is an object
# That means functions can be used as objects
# A decorator takes in a function, adds some functionality and returns it.


# Basic Decorator

def test_decorator(func):
    print('before')
    func()
    print('after')


@test_decorator
def do_stuff():
    print("Doing stuff")


# Real Decorator
# In this example we will change the functionality
def make_bold(func):
    def inner():
        print('<b>')
        func()
        print('</b>')

    return inner


@make_bold
def print_name():
    print('Alton')


print_name()


# Decorator with params
# Notice this has a defined number of parameters

def num_check(func):
    def check_int(o):
        if isinstance(0, int):
            if o == 0:
                print('Can not divide by zero')
                return False
            return True
        print('f{o} is not a number')
        return False

    def inner(x, y):
        if not check_int(x) or not check_int(y):
            return
        return func(x, y)

    return inner


@num_check
def divide(a, b):
    print(a / b)


divide(100, 3)
divide(0, 2)


# divide(100, 'cat')


# Decorator with unknown number of params
# We want a decorator that can pass params and handle anything
# We also want to chain them together

# *args **kwargs to the rescue

def outline(func):
    def inner(*args, **kwargs):
        print('-' * 20)
        func(*args, **kwargs)
        print(f'-'*20)
    return inner


def list_items(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        print(f'args = {args}')
        print(f'kwargs = {kwargs}')
        for x in args:
            print(f'arg={x}')
        for k,v in kwargs.items():
            print(f'key={k},value={v}')
    return inner




@outline  # this is run first
@list_items
def display(msg):
    print(msg)


display("hello")
