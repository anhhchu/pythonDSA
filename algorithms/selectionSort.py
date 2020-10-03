def selectionSort(arr):
    '''
    O(n^2) as there are 2 nested loops
    O(1) space as Swapping element in place
    '''
    
    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]: 
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


arr = [2,0,1,4,3]
selectionSort(arr)
print(arr)

arr = [8, 3, 1, 7, 0, 10,7,3, 2]
selectionSort(arr)     
print(arr)


arr = [1,0]
selectionSort(arr)     
print(arr)

arr = [1]
selectionSort(arr)     
print(arr)