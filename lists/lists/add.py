class Empty:
    def __init__(self):
        self.IsEmpty = True
Empty = Empty()

class Node:
    def __init__(self, value, tail):
        self.IsEmpty = False
        self.Value = value
        self.Tail = tail

def add(numb, list):
    x = list
    newl = Empty
    while not x.IsEmpty:
        sum = x.Value + numb
        newl = Node(sum, newl)
        x = x.Tail
    return newl
l = Empty
for i in range(3):
    cnt = i + 1
    l = Node(cnt, l)

list = add(10, l)
while not list.IsEmpty:
    print(list.Value)
    list = list.Tail