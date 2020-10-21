class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # heapsort, put all values in linkedlist to heap
        if not head:
            return head
        
        def heapify(arr,n,i): 
            smallest = i
            l = 2*i + 1
            r = 2*i + 2
            if l < n and arr[smallest] > arr[l]: smallest = l
            if r < n and arr[smallest] > arr[r]: smallest = r
            if smallest != i: 
                arr[i], arr[smallest] = arr[smallest], arr[i]
                heapify(arr, n, smallest)
            return arr
        
        arr = [] # O(n) space
        while head: # O(n)
            arr.append(head.val)
            head = head.next
            
        n = len(arr)
        # create a min heap
        for i in range(n//2-1, -1, -1):
            heapify(arr, n, i)
            
        head = ListNode()
        node = head
        for i in range(n-1, 0, -1):
            # swap value at i with 0
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0) 
            node.next = ListNode(arr.pop())
            node = node.next
            
        # add the last node arr[0] to linked list
        node.next = ListNode(arr.pop())
        return head.next