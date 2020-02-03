import random

def out_of_order(arr):
    #Algo works only on arrays tuples
    assert (type(arr) == list or type(arr) == tuple)
    
    count = 0

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j] < arr[i]:
                count += 1
    
    return count
arr = [1,2,3,4,5]

for i in range(5):
    random.shuffle(arr)
    print('\nThe array is ',arr)
    print('Brute Force Output: ',out_of_order(arr))
 