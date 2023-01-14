# Multiple Inheritance

# Inherit from multiple classes at the same time

class Vehical:
    speed = 0

    def drive(self, speed):
        self.speed = speed
        print('Driving')

    def stop(self):
        self.speed = 0
        print('Stopped')

    def display(self):
        print(f'Driving at {self.speed} speed')


class Freezer:
    temp = 0

    def freeze(self, temp):
        self.temp = temp
        print('Freezing')

    def display(self):
        print(f'Freezing at {self.temp} temp')


# FreezerTruck class
class FreezerTruck(Freezer, Vehical):  # Here we define the Method resolution Order
    def display(self):
        print(f'is a freezer:{issubclass(FreezerTruck, Freezer)}')
        print(f'is a vehicle:{issubclass(FreezerTruck, Vehical)}')

        #super(Freezer,self).display()# Works because of MRO
        #super(Vehical,self).display()# Fails because of MRO

        Freezer.display(self)
        Vehical.display(self)

t = FreezerTruck()
t.drive(50)
t.freeze(-50)
print('-' * 20)
t.display()  # Freezer display method without overriding would have been executed here
