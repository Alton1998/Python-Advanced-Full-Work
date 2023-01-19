# Exceptions
# Bad things happen, we need to know how to handle them

"""
Errors mostly occur at runtime that's they belong to an unchecked tpye.
Exceptions are the problems which can occur at runtime and compile time.
It mainly occurs in the code written by the developers
Exceptions are divided into 2 categories such as checked exceptions and unchecked exceptions.
"""


def outline(func):
    def inner(*args, **kwargs):
        print('-' * 20)
        func(*args, **kwargs)
        print(f'-' * 20)

    return inner


@outline
def test_one(x, y):
    try:
        z = x / y
        print(f'Result:{z}')
    except:
        print(f'Something bad happened x:{x}, y:{y}')
    finally:
        print('Complete')


@outline
def test_two(x, y):
    try:
        assert (x > 0)
        assert (y > 0)
    except AssertionError:
        print(f'Failed to assert x:{x},y:{y}')
    except Exception as e:
        print(f'Something bad happened x:{x}, y:{y}, issue:{e}')
    finally:
        print('Complete')


test_one(5, 0)
test_one(5, 'Cat')
test_one(1, 9)
test_two(0, 0)


# User defined exceptions and raising
class CatError(RuntimeError):
    def __init__(self, *args):
        self.args = args


@outline
def test_cats(qty):
    try:
        if not isinstance(qty, int):
            raise TypeError('Must be an int')
        if qty < 9:
            raise CatError("Must own more than 9 cats")
    except Exception as e:
        print(f'Opps:{e.args}')
    finally:
        print('Complete')


test_cats('abc')
test_cats(3)
test_cats(12.3)
