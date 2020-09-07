'''
base case: if len(arr) <= 1, return arr
divide array by half and call merge sort of each half
merge each half

O(nlogn) time as divide array by half and each merge takes linear time
O(n) space 
'''

def mergeSort(arr): 
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    L = mergeSort(arr[:mid])
    R = mergeSort(arr[mid:])

    return merge(L, R)

def merge(L, R): #merge 2 sorted array
    arr = []
    i, j = 0, 0

    while i < len(L) and j < len(R):
        #print(i, j, arr)
        if L[i] <= R[j]:
            arr.append(L[i])
            i += 1
        else:
            arr.append(R[j])
            j += 1

    arr += L[i:]
    arr += R[j:]

    return arr




print(merge([1,2,3], [0,4,6,8]))
print(merge([1, 2, 4],[0, 1, 3]))

  
print(mergeSort([2,0,1,4,3]))