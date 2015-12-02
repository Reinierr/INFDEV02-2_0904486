class Car:
    def __init__(self, var1, var2, var3):
        self.name = var1
        self.branch = var2
        self.price = var3
        self.wheels = Wheels(4, 20, "Black")
        self.inner = Inner("Green", "Leather", 50, "Mercedes", "Blue")
class Tyre:
    def __init__(self, var1, var2):
        self.inch = var1
        self.color = var2
class Wheels:
    def __init__(self, var1, var2, var3):
        self.amount = var1
        self.tyre = Tyre(var2, var3)
class Seat:
    def __init__(self, var1, var2):
        self.color = var1
        self.material = var2
class Engine:
    def __init__(self, var1, var2):
        self.temp = var1
        self.branch = var2
class Light:
    def __init__(self, var1):
        self.color = var1
class Inner:
    def __init__(self, var1, var2, var3, var4, var5):
        self.seat = Seat(var1, var2)
        self.engine = Engine(var3, var4)
        self.light = Light(var5)
var1 = raw_input('Car name: ')
var2 = raw_input('Car branch: ')
var3 = raw_input('Car price: ')
c = Car(var1, var2, var3)
print(c.name)
print(c.branch)
print(c.price)
print(c.wheels.amount)
print(c.wheels.tyre.color)
print(c.wheels.tyre.inch)
print(c.inner.engine.branch)
print(c.inner.engine.temp)
print(c.inner.light.color)
print(c.inner.seat.color)
print(c.inner.seat.material)