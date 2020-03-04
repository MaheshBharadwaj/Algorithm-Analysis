import time
import random
import math

def getMaxSum(x,start,end):
    #Singleton Element Base Case
    if start == end:
        if x[start] > 0 :
            return x[start]
        else:
            return 0
    
    #Adjacent Elements Base Case
    if start == end - 1:
        return max(x[start],x[end],x[start]+x[end])
    
    #4K + 2 split into 2k 2k + 2
    if (end - start + 1) % 4 == 2:
        mid = ((start + end) // 2) - 1
    else:
        mid = (start + end) // 2

    MaxLeft = getMaxSum(x,start,mid)
    MaxRight = getMaxSum(x,mid+1,end)

    thisLeftEdgeSum = 0 
    thisRightEdgeSum = 0
    maxLeftEdgeSum = 0
    maxRightEdgeSum = 0

    for i in range(mid,start - 1,-1):
        thisLeftEdgeSum += x[i]
        if(thisLeftEdgeSum > maxLeftEdgeSum):
            maxLeftEdgeSum = thisLeftEdgeSum

    for i in range(mid+1,end+1):
        thisRightEdgeSum += x[i]
        if(thisRightEdgeSum > maxRightEdgeSum):
            maxRightEdgeSum = thisRightEdgeSum

    return max(MaxLeft,MaxRight,maxLeftEdgeSum+maxRightEdgeSum)


print('+------+-------------+----------------+----------------+----------------+----------------+----------------+')
print('| %4s | %10s  | %14s | %14s | %14s | %14s | %14s | ' %('Size','Avg Time','N','N^2','N^3','Log N','N Log N'))
print('+------+-------------+----------------+----------------+----------------+----------------+----------------+')


for count in range(10):
    size = random.randint(200,700)
    sq = size ** 2
    cu = size ** 3
    lg = math.log(size)
    nlg = size * lg
    
    time_taken = 0      
    for iteration in range(10):
        inputList = []

        for i in range(size):       
            inputList.append(random.randint(-100,100))

        start_time = time.time()
        getMaxSum(inputList,0,size-1)
        end_time = time.time()
        time_taken += (end_time - start_time)
        avg_time = time_taken / 10

    print('| %4d | %11lf | %1.12lf | %1.12lf | %1.12lf | %1.12lf | %1.12lf |' % (size,avg_time,(avg_time/size),(avg_time/sq),(avg_time/cu),(avg_time/lg),(avg_time/nlg)))

print('+------+-------------+----------------+----------------+----------------+----------------+----------------+')

