from queue import PriorityQueue

class LinkedList:
    def __init__(self, val = 0):
        self.val = val
        self.next = None


class Solution:
    def sortList(self, head):
        # heapsort, put all values in linkedlist to heap
        if not head:
            return head
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        arr.sort(reverse=True)
        
        curr = head
        while curr:
            curr.val = arr.pop()
            curr = curr.next
            
        return head

    def sortListPQ(self, head): # sort list with priority queue
        if not head:
            return head
        q = PriorityQueue()
        curr = head
        while curr: 
            q.put(curr.val)
            curr = curr.next
        curr = head
        while not q.empty():
            curr.val = q.get()
            curr = curr.next
        return head
        
