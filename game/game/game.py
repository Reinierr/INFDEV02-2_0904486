import sys, pygame, time
pygame.init()

class Car:
    def __init__(self, image, x, y):
        self.image = image
        self.posX = x
        self.posY = y

class Empty:
    def __init__(self):
        self.IsEmpty = True
Empty = Empty()

class Node:
    def __init__(self, value, tail):
        self.IsEmpty = False
        self.Value = value
        self.Tail = tail

car1 = Car("auto.png", 100, 0)
car2 = Car("auto2.png", 400, 0)
car3 = Car("auto3.png", 700, 0)

l = Empty
l = Node(car1, l)
l = Node(car2, l)
l = Node(car3, l)

x = True
size = width, height = 1024, 768
screen = pygame.display.set_mode(size)
newL = l

while not newL.IsEmpty:
    print(newL.Value.image)
    carimg = pygame.image.load(newL.Value.image)
    carrect = carimg.get_rect()
    carrect = carrect.move([0, 2])
    posx = newL.Value.posX
    posy = newL.Value.posY
    pos = [posx, posy]
    newL = newL.Tail

while x:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: x = False


    screen.blit(carimg, carrect)
    pygame.display.flip()

    
    
    
