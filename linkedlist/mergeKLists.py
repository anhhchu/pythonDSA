class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        '''
        O(NlogN) time and O(N) space
        '''  
        arr = []
        for l in lists:
            #head = l
            while l:
                arr.append(l.val)
                l = l.next
                
        arr.sort(reverse = True)
    
        head = ListNode()
        curr = head
        while arr:
            curr.next = ListNode(arr.pop())
            curr = curr.next
 
        return head.next

    def mergeKListsDC(self, lists): # divide and conquer
        '''
        O(Nlogk) time where k is the len of lists and N is number of elements in all lists. 
        O(1) space, merging happening in place
        '''

        def merge(l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1
            if l1.val <= l2.val: 
                l1.next = merge(l1.next, l2)
                return l1
            if l2.val < l1.val:
                l2.next = merge(l1, l2.next)
                return l2

        if len(lists) == 0:
            return
        if len(lists) == 1: 
            return lists[0]
        
        mid = len(lists)//2
        
        L = self.mergeKLists(lists[:mid])
        R = self.mergeKLists(lists[mid:])
        return merge(L, R)

l1 = ListNode(4, ListNode(3,ListNode(2, ListNode(1))))
l2 = ListNode(5, ListNode(2,ListNode(1, ListNode(0))))
lists = []
lists.append(l1)
lists.append(l2)
print(lists)

sol = Solution()
ll = sol.mergeKListsDC(lists)
while ll:
    print(ll.val)
    ll = ll.next

        
        
        