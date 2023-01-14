class Feline:
    def __init__(self, name):
        self.name = name
        print('Creating a feline')

    def meow(self):
        print(f'{self.name}:meow')

    def set_name(self, name):
        print(f'{self} setting name :{name}')


class Lion(Feline):
    def roar(self):
        print(f'{self.name} roar')

class Tiger(Feline):
    # override the constructor is a bad idea unless you know what you are doing
    def __init__(self):
        # super allows us to access the parent
        # if we forget this we will have a bad time later
        super().__init__('No Name')
        print('Creating a Tiger')

    def stalk(self):
        # have to make sure name is set in the parent
        # this is considered LBYL (look before you leap)
        # here we are dynamically adding the attribute

        # if we did not init the super we will have to be careful
        # if not hasattr(self,'name'): super().setName('No Name')
        print(f'{self.name}: stalking')

    def rename(self,name):
        super().set_name(name)


c = Feline('kitty')
print(c)
c.meow()

l = Lion('leo')
print(l)
l.meow()
l.roar()

t = Tiger() # is a Feline with a different constructor
print(t)
t.stalk()
t.rename('Tony')
t.stalk()