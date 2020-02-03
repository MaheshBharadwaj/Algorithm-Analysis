'''
Incorrect Algorithm
'''

def out_of_order_imp(arr):
    assert (type(arr) == list or type(arr) == tuple)
    
    count = 0

    def merge_sort(arr):
        nonlocal count

        #print(arr)

        start = 0
        end = len(arr) - 1
        '''
        if len(arr) <= 1:
            return arr
        '''
        if len(arr) == 1:
            return arr
        if len(arr) == 2:
            count +=1
            if arr[0] < arr[1]:
                return arr
            else :
                arr[0],arr[1] = arr[1],arr[0]
                return arr

       

        
        if (end - start + 1) % 4 == 2:
            middle = (start + end) // 2 - 1
        else:
            middle = (start + end)//2
        
        #middle = (start + end) // 2 
        left_sorted = merge_sort(arr[start:middle+1])
        right_sorted = merge_sort(arr[middle+1:end+1])
    
        len_l = len(left_sorted)
        len_r = len(right_sorted)
        i = j = 0
        merged_array = []
        #print('merging',left_sorted,'with',right_sorted)
        while i < len_l and j < len_r:
            if left_sorted[i] < right_sorted[j]:
                merged_array.append(left_sorted[i])
                i += 1
            else:
                merged_array.append(right_sorted[j])
                count += 1
                j += 1

        while i < len_l:
                merged_array.append(left_sorted[i])
                i += 1
                count += 1
        while j < len_r:
                merged_array.append(right_sorted[j])
                j += 1 
                #count += 1
        return merged_array

    print('The sorted arrays is: ',merge_sort(arr))
    return count


print('The number of pairs: ',out_of_order([2,3,5,1,4]))
print('The number of pairs: ',out_of_order([4,3,5,1,2]))