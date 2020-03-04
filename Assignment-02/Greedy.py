import time
import random
import math

def getMaxSum(x):
	n = len(x)
	thisSum = 0
	maxSum = 0
	for i in range(n):
		thisSum += x[i]
		if thisSum > maxSum:
			maxSum = thisSum
		elif thisSum < 0:
			thisSum = 0
		else:
			pass
	return maxSum

print('+---------+-------------+------------------+------------------+------------------+------------------+------------------+')
print('| %7s | %10s  | %16s | %16s | %16s | %16s | %16s | ' %('Size','Avg Time','N','N^2','N^3','Log N','N Log N'))
print('+---------+-------------+------------------+------------------+------------------+------------------+------------------+')


for count in range(10):

	size = random.randint(100,1000)
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

	print('| %7d | %11lf | %1.14lf | %1.14lf | %1.14lf | %1.14lf | %1.14lf |' % (size,avg_time,(avg_time/size),(avg_time/sq),(avg_time/cu),(avg_time/lg),(avg_time/nlg)))

print('+---------+-------------+------------------+------------------+------------------+------------------+------------------+')

