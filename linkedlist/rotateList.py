# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRightRecursion(self, head, k): # Runtime Error when list or k is too big
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head 
        #self.printLL(head)
        if k == 0:
            return head
        #             ll
        # 1->2->3->4->5->NONE
        else:
            node = head
            prev = None
            while node.next: # stop at node = 5, prev = 4
                prev = node 
                node = node.next  

            # tail found
            newNode = ListNode(node.val)

            newNode.next = head # link newNode to head
            prev.next = None # delete node

            # do it until k is 0
            k -= 1
            return self.rotateRightRecursion(newNode, k)
            
    def rotateRightIterative(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        O(n) where n is len linked list 
        """
        #             ll
        # 1->2->3->4->5->NONE
        
        if head is None or head.next is None:
            return head 
        
        # get len of linkedlist
        # if k % len(ll), the list will revert back to original list
        node, count = head, 0
        while node: #O(n)
            count += 1
            node = node.next 
            
        j = k%count 
        while j > 0: # only check the modulus of k and len(linkedlist)
            node = head # reset node
            prev = None # reset prev
            while node.next: # stop at node = 5, prev = 4
                prev = node 
                node = node.next  
            # tail found
            prev.next = None # disconnect node
            
            #newNode = ListNode(node.val)
            node.next = head # link newNode to head
            head = node
            
            j -= 1
        
        return head 

    def rotateRightCircular(self, head, k):
        if head is None or head.next is None:
            return head
        # create a ring by connecting tail with head, and identify the len of linked list
        tail, n = head, 1
        while tail.next:
            tail = tail.next
            n += 1
        # close the loop
        tail.next = head

        i = n - k%n
        # identify the position to cut the ring
        while i > 0: 
            tail = tail.next
            head = head.next
            i -= 1
        # cut the ring
        tail.next = None
        return head

        
    def printLL(self, head):
        node = head
        result = []
        while node: 
            result.append(node.val)
            node = node.next
        print(result)
        


sol = Solution()

ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
sol.printLL(ll)
rotatedList = sol.rotateRightIterative(ll, 1150005)
sol.printLL(rotatedList)

ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
rotatedList2 = sol.rotateRightCircular(ll, 1150005)
sol.printLL(rotatedList2)


            