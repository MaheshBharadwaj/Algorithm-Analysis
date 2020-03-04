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

arr = readArray()
num = int(input('Enter the number to insert: '))
print('The target index is:',linear_locate(num,arr,0))
        