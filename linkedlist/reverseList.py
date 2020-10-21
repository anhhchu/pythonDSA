'''
Reverse Linked List 2 ways: iterative and recursive
'''

class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseListIterative(self, head):
        '''
        O(N) with N is number of elements
        O(1) space
        '''
        prev = None

        # 1 -> 2 -> 3 -> 4 -> 5 -> N
        # prev = None, head = 1 ->, nxt = 2 -> 
      
        while head: 
            nxt = head.next # 3 -> 4 -> 5 -> N
            head.next = prev # 2 -> 1 -> None
            prev = head # prev = 2 -> 1 -> None
            head = nxt # head = 3 -> 4 -> 5 -> N

        return prev

    def reverseListRecursive(self, head):
         # 1 -> 2 -> 3 -> 4 -> 5 -> N
        def reverseList(head, prev):
            # 3. head = 2 -> 3 -> ..., prev = 1 -> None
            if head is None: 
                return prev
            nxt = head.next # nxt = 3 -> 4 -> 5 -> N
            head.next = prev # head = 2 -> 1 -> N
            prev = head # prev = 2 -> 1 -> 
            return reverseList(nxt, prev) 
        
        return reverseList(head, None)


#ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
ll = [1]

sol = Solution()
#head = sol.reverseListIterative(ll)
head = sol.reverseListRecursive(ll)
result = []
while head:
    result.append(head.val)
    head = head.next
print(result)


