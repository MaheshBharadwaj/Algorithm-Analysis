import random
import time
import math

from Point import Point
from Queue import LinkedQueue

class Tree(object):
    __slots__  = ['data','left','right','ref']


    def __init__(self,data=[],ref=None):
        assert type(data) == list
        self.data = data
        self.ref = ref
        self.left = None
        self.right = None

    def insert(self,data):
        assert type(data) == Point
        
        if len(self.data) == 0:
            self.data.append(data)
            return
        
        if self.ref.distance(data) < self.ref.distance(self.data[0]):
            if self.left is None:
                self.left = Tree([data],self.ref)
            else:
                self.left.insert(data)
        elif self.ref.distance(data) > self.ref.distance(self.data[0]):
            if self.right is None: 
                self.right = Tree([data],self.ref)
            else:
                self.right.insert(data) 
        else:
            #Same distance[ie Lies on same circle]
            self.data.append(data)

    def inorder(self):
        if self.left is not None:
            yield from self.left.inorder()
        
        yield from self.data

        if self.right is not None:
            yield from self.right.inorder()

print("To Check Algorith Correctness: ")
n = 0
q = LinkedQueue()
print('Enter the number of points: ')
n = int(input())
print('Enter the points[x,y]: ')

for i in range(n):
    x,y = tuple(map(float,input().split()))
    q.enqueue(Point(x,y))

print('Enter the referance point[x,y]: ')
x,y = tuple(map(float,input().split()))
refPoint = Point(x,y)


t = Tree(list(),refPoint)

while q.isEmpty() == False:
    t.insert(q.dequeue())


for point in t.inorder():
    print('Point Enqueued' + str(point))
    q.enqueue(point)

print("\nFinding Time Complexity: \n\n")

print("+-----------+----------------+--------------------+----------------+----------------+")
print("|   Size    |       N        |         N^2        |     N Log N    |   Time Taken   |")
print("+-----------+----------------+--------------------+----------------+----------------+")

length = random.randint(29000,30000)


for iter in range(20):
    q = LinkedQueue()
    t = Tree([],refPoint)
    for size in range(length):
        q.enqueue(Point(random.randint(-100,100),random.randint(-200,350) ))
    
    #Queue with values is now ready
    start = time.time()
    
    while q.isEmpty() == False:
        t.insert(q.dequeue())
    

    for point in t.inorder():
        q.enqueue(point)
    #Result stored in 'q'
    end = time.time()
    timeTaken = (end-start)

    print("| %9d | %14.12f | %18.16f | %14.12f | %14.12f |" % (length,(timeTaken /length),(timeTaken/(length**2)),(timeTaken/(length * math.log(length))),timeTaken))
    length += 2000

print("+-----------+----------------+--------------------+----------------+----------------+")
