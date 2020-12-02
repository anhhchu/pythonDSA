# Definition for singly-linked list.
class ListNode:
        def __init__(self, val, next):
            self.val = val
            self.next = next

import random
class Solution:

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        scope = 1
        res = 0
        curr = self.head
        
        while curr:
            if random.random() < 1/scope:
                res = curr.val
            curr = curr.next
            scope += 1
            
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()