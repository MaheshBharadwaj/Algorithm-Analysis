def readArray(i):
    inp = input('Enter the elements of array ' + str(i) + ': ')
    arr = list(map(int,inp.split()))
    return arr  

def merge(arr1,arr2,res):
    if len(arr1) and len(arr2):
        if arr1[0] < arr2[0]:
            res.append(arr1[0])
            return merge(arr1[1:],arr2,res)
        else:
            res.append(arr2[0])
            return merge(arr1,arr2[1:],res)

    elif len(arr1):
        res += arr1
        return res
    elif len(arr2):
        res += arr2
        return res
    else:
        return res


arr1 = readArray(1)
arr2 = readArray(2)

res = []

res = merge(arr1,arr2,res)

print(res)