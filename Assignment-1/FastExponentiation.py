import sys

def toBinary(n):
	bVal = []
	while n:
		bVal.append(n%2)
		n = (n // 2)
	bVal.reverse()
	return bVal


def multiply(m1,m2):
	r1 = len(m1)
	c1 = len(m1[0])
	
	r2 = len(m2)
	c2 = len(m2[0])

	res=[[0 for col in range(c2)] for row in range(r1)]
	

	for i in range(r1):
		for j in range(c2):
			for k in range(r2):
				res[i][j]+= m1[i][k] * m2[k][j]

	return res

def FastExp(mat,n):
	saved ={1:mat,2:multiply(mat,mat)}

	def computeExponent(mat,n):
		if n in saved:
			return saved[n]
		saved[n] = multiply(computeExponent(mat,n//2),computeExponent(mat,n//2))
		return saved[n]
	
	r = len(mat)
	c = len(mat[0])

	#Initialising identity matrix	
	ans = [[0 for row in range(r)] for col in range(c)]
	for i in range(r):
		ans[i][i] = 1
	
	bin = list(toBinary(n))

	for i in range(len(bin)):
		if bin[i] == 1:
			ans = multiply(ans,computeExponent(mat,2 ** (len(bin) - i -1 )))
	return ans

mat = [[1,4,3],[0,4,1],[1,4,2]]

n = int(input("Enter the required exponent: "))
if n  == 0:
	print(mat)
elif n < 0:
	print("Error!Please Provide Positive value")
else:
	print("The matrix is\n",mat)
	print("Resulting Matrix is\n",FastExp(mat,n))

