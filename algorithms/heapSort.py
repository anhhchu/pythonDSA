'''
Heapsort
A heapsort is an in-place sorting algorithm that treats an array like a binary tree and moves the largest values to the end of the heap until the full array is sorted.

The main steps in a heapsort are: 
1. Convert the array into a maxheap (a complete binary tree with decreasing values) 
2. Swap the top element with the last element in the array (putting it in it's correct final position) 
3. Repeat with arr[:len(arr)-1] (all but the sorted elements)
'''

def heapsort(arr):
    heapify(arr, len(arr), 0)
    
def heapify(arr, n, idx):
    """
    :param: arr - array to heapify
    n -- number of elements in the array
    i -- index of the current node
    TODO: Converts an array (in place) into a maxheap, a complete binary tree with the largest values at the top
    """
    for val in arr: 
        pass

