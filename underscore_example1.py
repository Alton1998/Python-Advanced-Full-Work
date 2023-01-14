class Person:
    ## Weak Private
    _name = 'No Name'

    def set_name(self, name):
        self._name = name
        print(f'Name set to {self._name}')

    ## Strong Private
    def __think(self):
        print('Thinking to my self')

    def work(self):
        self.__think()

    ## This is going to be internal to the class also we want to avoid naming conflicts (Mangling)
    def __init__(self):
        print('Constructor')

    def __call__(self):
        print('Call Someone')


class Child(Person):
    def test_double(self):
        self.__think(self)
