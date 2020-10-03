'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not (l1 and l2):
            return 
        elif not l1: 
            return l2
        elif not l2:
            return l1
        
        l3 = ListNode()
        node = l3
        carry = 0
        
        # continue until l1, l2 and carry are all None
        # remember carry!!!
        while l1 or l2 or carry: 
            v1 = l1.val if l1 else 0  
            v2 = l2.val if l2 else 0
            val = v1+v2
            
            r = (val + carry)%10
            node.next = ListNode(r)
            carry = (val+carry)//10
            
            node = node.next
            
            # go to next node but remember to check for None Node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
    
        
        if l1:
            node.next = l1.next
        if l2:
            node.next = l2.next
            
        # return l3.next as the first value of l3 is set to 0 in l3 = ListNode()
        return l3.next


def LinkedList(arr):
    ll = ListNode(arr[0])
    node = ll
    for num in arr[1:]:
        node.next = ListNode(num)
        node = node.next

    return ll
    
l1 = LinkedList([2,4,3])
l2 = LinkedList([5,6,4])

sol = Solution()
print(sol.addTwoNumbers(l1,l2).val)
        
            
        