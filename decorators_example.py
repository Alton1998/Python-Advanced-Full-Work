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
