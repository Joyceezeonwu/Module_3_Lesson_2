#creating a class car

class Car:
    def __init__(self,brand,model,color,fuel,size):
        self.brand=brand
        self.model=model
        self.color=color
        self.fuel=fuel
        self.size=size
    def start(self):
        print('car is moving')
    def halt(self):
        print('car stops')
    def drift(self):
        print('car turns right')
    def speedup(self):
        print('moves really fast')
    def turn(self):
        print('makes a U-turn')

properties = Car('Toyota', 'Corolla', 'Black', 'PMS', 'Big')

print('This car has the following attributes')
print(properties.brand)
print(properties.model)
print(properties.color)
print(properties.fuel)
print(properties.size)




