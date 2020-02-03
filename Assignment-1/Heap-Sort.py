def readArray():
    inp = input('Enter the elements of array: ')
    arr = list(map(int,inp.split()))
    return arr  

def heap_sort(arr):
    i = 0
    while 2 ** (i + 1) < len(arr):
        if arr[2 ** i] > arr[2 ** (i + 1)]:
            arr[2 ** i],arr[2 ** ( i + 1)] = arr[2 ** (i + 1)],arr[2 ** i]
            i = i + 1
        else: 
            break
    return arr

arr = readArray()
print('The input array is:',arr)
print('The Sorted Array is:',heap_sort(arr))