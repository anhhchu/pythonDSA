'''
Heapsort
A heapsort is an in-place sorting algorithm that treats an array like a binary tree and moves the largest values to the end of the heap until the full array is sorted.

The main steps in a heapsort are: 
1. Convert the array into a minheap (a complete binary tree with increasing values) 
2. At this point, the largest item is stored at the root of the heap. Replace it with the last item of the heap followed by reducing the size of heap by 1. Finally, heapify the root of the tree.
3. Repeat step 2 while size of heap is greater than 1.

Time complexity:
O(NlogN) which O(logN) for heapify process
O(1) space, everything happening in place
'''


def heapsort(arr):
        n = len(arr)
        # build max heap out of elements
        for i in range(n//2-1, -1, -1): # O(logN)
                heapify(arr, n, i)
        print(arr) # arr after heapify will be a maxheap with max element in the front

        # rearrange the array
        for i in range(n-1, 0, -1): # loop from end of array, O(N)
                arr[0], arr[i] = arr[i], arr[0] # bring small values to the front
                heapify(arr, i, 0) # heapify the root to bring the large values to the front for swapping in next iteration # O(logN)
        
        return arr
    
def heapify(arr, n, i): 
        """
        :param: arr - array to heapify
        n -- number of elements in the array
        i -- index of the current node
        Converts an array (in place) into a maxheap, a complete binary tree with the largest values at the top

        O(logn) for heapify 
        """
        # largest index is i
        largest = i
        l = i*2 + 1
        r = i*2 + 2
        if l < n and arr[l] > arr[i]:
                largest = l
        if r < n and arr[r] > arr[largest]:
                largest = r
        # change root if needed
        if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

arr =  [4,3,2,1] #[ 10, 11, 5, 14, 7] 
print(heapsort(arr))




