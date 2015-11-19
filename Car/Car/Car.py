class Tyre:
    def __init__(self, type, inch):
        self.type = type
        self.inch = str(inch)
class Wheels:
    def __init__(self, amount):
        self.amount = str(amount)
class Engine:
    def __init__(self, temp, pk):
        self.temp = str(temp)
        self.pk = str(pk)
class Seat:
    def __init__(self, color, amount):
        self.color = color
        self.amount = str(amount)
class Light:
    def __init__(self, light):
        self.light = light
class Person:
    def __init__(self, driver, passengers):
        self.driver = driver
        self.passengers = str(passengers)
class Car:
    def __init__(self, tyretype, tyreinch, wheelamount, enginetemp, enginepk, seatcolor, seatamount, light, drivername, passageramount):
        self.tyre = Tyre(tyretype, tyreinch)
        self.wheels = Wheels(wheelamount)
        self.engine = Engine(enginetemp, enginepk)
        self.seat = Seat(seatcolor, seatamount)
        self.light = Light(light)
        self.person = Person(drivername, passageramount)
        
car = Car("Continental", 22, 4, 50, 150, "Red", 4, "Bright", "Freek", 3)

print("Car info: \n")
print(car.wheels.amount+" tyres of the type: "+car.tyre.type+" Size: "+car.tyre.inch+" inch")
print("Current engine temperature: "+car.engine.temp+" Horsepower: "+car.engine.pk)
print(car.seat.amount+" "+car.seat.color+" seats.")
print(car.light.light+" lights")
print("The current driver is: "+car.person.driver)
print("The car has "+car.person.passengers+" passengers")