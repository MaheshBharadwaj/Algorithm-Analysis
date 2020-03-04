bolts = list(map(int,input().split()))
nuts  = list(map(int,input().split()))

def partition(input_arr,pivot):
	res_l = []
	res_r = []
	for i in input_arr:
		if i < pivot:
			res_l.append(i)
		elif i > pivot:
			res_r.append(i)
	index = len(res_l)
	res_l.extend([pivot])
	res_l.extend(res_r)
	
	return res_l,index

res_nuts = []
res_bolts = []

def solve(nuts,bolts):
	global res_nuts
	global res_bolts
	if len(nuts) == 0:
		return
	if len(nuts) == 1:
		res_nuts.extend(nuts)
		res_bolts.extend(bolts)
		return	

	pivot = nuts[ len(nuts) // 2 ]
	bolts,index  = partition(bolts,pivot)
	nuts,index = partition(nuts,bolts[index])
	solve(nuts[:index],bolts[:index])
	res_nuts.append(pivot)
	res_bolts.append(pivot)
	solve(nuts[index+1:],bolts[index+1:])


solve(nuts,bolts)
print(res_nuts)
print(res_bolts)

