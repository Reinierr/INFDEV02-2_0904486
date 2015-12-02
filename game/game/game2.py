import sys, pygame
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

size = width,height = 1024,768
speed = [0,2]
black = 0,0,0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("auto.png")
ballrect = ball.get_rect()
x = True
while x:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.bottom > height:
        

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()