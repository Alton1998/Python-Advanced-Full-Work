# Map
# Looping without a loop
# Maps function calls to a collection of items
# map (func, iterables)

# Basic usage - Count len
people = ["Alton", "STeve", "HYde"]

counts = []
for x in people:
    counts.append(len(x))

print(f'Old way :{counts}')

print(f'Mapped: {list(map(len, people))}')

# More complex - Combine Elements
# Notice different lens, we are also passing multiple args

firstname = ('Apple', 'Choclate', 'Fudge', 'Pizza')
lastnames = ('Pie', 'Cake', 'Brownies')


def merg(a, b):
    return a + ' ' + b


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def doall(func, num):
    return func(num[0], num[1])


x = map(merg, firstname, lastnames)
print(x)
print(list(x))

f = (add, subtract, multiply, divide)
v = [[5, 3]]
n = list(v) * len(f)

print(f'f:{f},n:{n}')

m = map(doall, f, n)
print(list(m))
