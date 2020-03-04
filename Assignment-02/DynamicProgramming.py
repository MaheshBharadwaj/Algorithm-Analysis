import time
import random
import math

def getMaxSum(x):
	n = len(x)
	maxSum = 0
	for i in range(n):
		thisSum = 0
		for j in range(i,n):
			thisSum += x[j]
			if thisSum > maxSum:
				maxSum = thisSum
	return maxSum
print('+------+-------------+----------------+----------------+----------------+----------------+----------------+')
print('| %4s | %10s  | %14s | %14s | %14s | %14s | %14s | ' %('Size','Avg Time','N','N^2','N^3','Log N','N Log N'))
print('+------+-------------+----------------+----------------+----------------+----------------+----------------+')


for count in range(10):
	size = random.randint(1000,5000)
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
		getMaxSum(inputList)
		end_time = time.time()
		time_taken += (end_time - start_time)
		avg_time = time_taken / 10

	print('| %4d | %11lf | %1.12lf | %1.12lf | %1.12lf | %1.12lf | %1.12lf |' % (size,avg_time,(avg_time/size),(avg_time/sq),(avg_time/cu),(avg_time/lg),(avg_time/nlg)))

print('+------+-------------+----------------+----------------+----------------+----------------+----------------+')

