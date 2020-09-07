'''
Choose a pivot, arrange elements so that element to the left <= pivot, element to the right > pivot
Divide and Conquer with O(nlogn) time. Can be O(n^2) when the pivot is either too high or too low. 
O(1) inplace for space: As per the broad definition of in-place algorithm it qualifies as an in-place sorting algorithm 
as it uses extra space only for storing recursive function calls but not for manipulating the input.

'''

def quickSort(arr):
    
    if len(arr) <= 1: return arr

    pivotIdx = len(arr) - 1
    
    # iterate to sort elements according to pivot 
    i = pivotIdx - 1
    while i >= 0: 
        if arr[i]  > arr[pivotIdx]: 
            arr[i], arr[pivotIdx] = arr[pivotIdx], arr[i] # swap value
            pivotIdx = i
            i -= 1
        else: 
            i -= 1

    print((pivotIdx, arr[pivotIdx]))
    print(arr)
    return quickSort(arr[:pivotIdx]) + [arr[pivotIdx]] + quickSort(arr[pivotIdx+1:])     

arr = [2, 0, 1, 4, 3]
print(quickSort(arr))
