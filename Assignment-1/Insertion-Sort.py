def readArray():
    inp = input('Enter the elements of array: ')
    arr = list(map(int,inp.split()))
    return arr  

def linear_locate(x,l,index):
    if len(l) == 0:
        return index
    elif x > l[0]:
        index = index + 1
        return linear_locate(x,l[1:],index)
    else:
        return index


def ordered_insert(x,l):
    #Target index
    index = linear_locate(x,l,0)
    l = l[:index] + [x] + l[index:]
    return l 

def insertion_sort(arr):
    if len(arr) == 1:
        return arr
    else :
        return ordered_insert(arr[0],insertion_sort(arr[1:]))

arr = readArray()

print('The sorted Array:',insertion_sort(arr))