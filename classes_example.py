# Introduction to classes

# OOP - object-oriented programming
# Blue prints for creating objects
# Classes are a big topic
# self is the first param

class Cat:
    name = ''
    age = 0
    color = ''

    # constructor
    def __init__(self, name, age=0, color='white'):
        self.name = name
        self.age = age
        self.color = color
        print(f'Constructor for {self.name}')

    def meow(self):
        print(f'{self.name} meow')

    def sleep(self):
        print(f'{self.name} zzz')

    def hungry(self):
        for x in range(5):
            self.meow()

    def eat(self):
        print(f'{self.name} nom nom nom')


x = Cat(name='brfdsfsf', age=10, color='blue')
x.meow()
