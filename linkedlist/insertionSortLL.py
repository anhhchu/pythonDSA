# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def insertionSortList(self, head): # return List Node
        if not head:
            return 
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            if curr.val < head.val: # bring to head
                prev.next = nxt
                curr.next = head
                head = curr
                curr = nxt
            
            elif prev and prev.val > curr.val: # need to move the node
                
                prev2 = None
                node = head
              
                while node and node.val <= curr.val: # go from head to node less than curr node
                    prev2 = node
                    node = node.next
                #if node.val > curr.val: # found the place to swap, bring curr to before node
               
                prev.next = nxt
                curr.next = node
                prev2.next = curr
                curr = nxt
   
            else:
                prev = curr
                curr = curr.next
                
        return head
                        
        