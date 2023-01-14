# The underscore
# Often ignored but there are multiple usecases
# _single
# __Double
# __Before
# After__
# __Both__

from underscore_example1 import *

# Skipping
for _ in range(5):
    print('Hello')

# Before(Single)
# Internal use only , called a weak private

p = Person()
p.set_name('Bryan')
print(f'Weak private {p._name}')
p._name = 'NOOOOOOOOO' # should never do this
print(f'Weak Private {p._name}')

# Before (Double)
# Internal use only, avoid conflict in subclass
# and tells python to rewrite the name (Mangling)
p = Person()
p.work()
#p.__think()
# c = Child()
# c.test_double()

# After (any)

# Helps to avoid naming conflicts with key words
class_ = Person()

print(dir(class_))

# Before and after
# Considered special to python, like the init and main function

p = Person()
p.__call__()

