class Empty:
    def __init__(self):
        self.IsEmpty = True
Empty = Empty()

class Node:
    def __init__(self, value, tail):
        self.IsEmpty = False
        self.Value = value
        self.Tail = tail

def filterEven(list):
    x = list
    while not x.IsEmpty:
        if x.Value % 2 == 0:

        x = x.Tail
    return newl

l = Empty
for i in range(3):
    cnt = i + 1
    l = Node(cnt, l)

list = filterEven(l)
while not list.IsEmpty:
    print(list.Value)
    list = list.Tail