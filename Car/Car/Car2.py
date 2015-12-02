class Car:
    def __init__(self, var1, var2, var3):
        self.tyre = Tyre("Continental")
        self.wheels = Wheels("Blue", 4)
        self.engine = Engine("Renault", 50, 100)
        self.seat = Seat("Red")
        self.person = Person("Freek")
class Tyre:
    def __init__(self, var1):
        self.var1 = var1
class Wheels:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
class Engine:
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3
class Seat:
    def __init__(self, var1):
        self.var1 = var1
class Person:
    def __init__(self, var1):
        self.var1 = var1

car = Car("test", "test", "test")

print(car.person.var1)