# Iterators
import random

t = (1,2,3,4)

for x in t:
    print(x)


# Iter Basics
# Lists, tuples, dictionaries and sets are all iterable objects

people = ['Bryan','Tammy','Rango']
i = iter(people)
print(i)
print(next(i))
print(next(i))
print(next(i))
# print(next(i)) # StopIteration

# Iterable class

class Lotto:
    def __init__(self):
        self._max = 4

    def __iter__(self):
        # The yield statement function's execution
        # and sends a value back to the caller, but retains enough
        # State to enable funtion to resume where it is left off
        for _ in range(self._max):
            yield random.randrange(0,100)

    def setMax(self,value):
        self._max = value

print('-'*20)
lottp = Lotto()
lottp.setMax(50)

for x in lottp:
    print(x)

print('-'*20)