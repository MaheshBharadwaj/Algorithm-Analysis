def readArray():
    inp = input('Enter the elements of array: ')
    arr = list(map(int,inp.split()))
    return arr  

'''
Iterative
def minimum(a):
	min_index = 0
	for i in range(1,len(a)):
		if(a[i]<a[min]):
			min_index = i
	return min_index

'''
def minimum(arr,low,high):
	l = arr[low:high]
	min = 0
	for i in range(1,len(l)):
		if l[i] < l[min]:
			min = i 
	return (min + low)

def selection_sort(arr):
	for i in range( len(arr) - 2):
		arr [ minimum(arr,i,len(arr)) ] , arr[i] = arr[i] , arr[ minimum(arr,i,len(arr)) ]
	return arr

print('Testing for 4 cases\n')
for i in range(4):
	arr = readArray()
	print('The input array is: ',arr)
	print('The sorted array is : ',selection_sort(arr))

