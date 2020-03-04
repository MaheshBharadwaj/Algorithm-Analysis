bolts = list(map(int,input().split()))
nuts  = list(map(int,input().split()))


for i in range(len(bolts) - 1):
	for j in range(i,len(nuts)):
		if nuts[j] == bolts[i]:
			nuts[j],nuts[i] = nuts[i],nuts[j]
			break
		
print(nuts)
print(bolts)
