def readArray(i):
    inp = input('Enter the elements of array ' + str(i) + ': ')
    arr = list(map(int,inp.split()))
    return arr

def ordered_merge(a1,a2):
    res = []
    
    i = 0
    j = 0

    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            res.append(a1[i])
            i = i + 1
        else:
            res.append(a2[j])
            j = j + 1
    
    if i != len(a1):
        res  = res + a1[i:]
    elif j != len(a2):
        res = res + a2[j:]
    else:
        pass

    print(res)

arr1 = readArray(1)
arr2 = readArray(2)
ordered_merge(arr1,arr2)
            