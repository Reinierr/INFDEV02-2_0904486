class Tyre:
    def __init__(self, var1, var2):
        self.inch = var1
        self.branch = var2
class Wheels:
    def __init__(self, var1, var2, var3):
        self.amount = var1
        self.tyre = Tyre(var2, var3)
class Engine:
    def __init__(self, var1, var2):
        self.temp = var1
        self.pk = var2
class Seat:
    def __init__(self, var1, var2, var3):
        self.color = var1
        self.material = var2
        self.amount = var3
class Person:
    def __init__(self, var1, var2):
        self.driver = var1
        self.passengers = var2
class Car:
    def __init__(self, var1, var2, var3):
        self.name = var1
        self.branch = var2
        self.price = var3
        self.wheels = Wheels(4, 20, "Continental")
        self.engine = Engine(50, 150)
        self.person = Person("Hendrik", 3)
        self.seat = Seat("Red", "Leather", 4)

c = Car("Astra", "Opel", 15000)
print(c.wheels.tyre.branch)
print(c.wheels.tyre.inch)
print(c.engine.pk)