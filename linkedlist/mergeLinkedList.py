'''
merge 2 sorted linked lists
sorted linked list 
'''

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next
#           l1
# 2 -> 5 -> 10 -> None
#                l2
# 3 -> 4 -> 5 -> 7 -> 12 -> None
#                              head
# 0 -> 2 -> 3 -> 4 -> 5 -> 7 -> 10 

def mergeListIterative(l1, l2):
    l3 = ListNode(0)
    head = l3 # 0 -> None

    while l1 and l2: # go until either list ends
        if l1.val <= l2.val: # 2 vs 3
            head.next = ListNode(l1.val)
            l1 = l1.next

        elif l1.val >= l2.val: # 5 vs 3
            head.next = ListNode(l2.val)
            l2 = l2.next

        head = head.next 

    remain = l1 if l1 else l2

    head.next = remain 

    return l3.next

def mergeListRecursively(l1,l2): 
    # base case
    if not l1:
        return l2
    if not l2:
        return l1
    if l1.val <= l2.val:
        l1.next = mergeListRecursively(l1.next, l2) # advance l1
        return l1
    if l1.val > l2.val:
        l2.next = mergeListRecursively(l1, l2.next)
        return l2
    

def test(l1, l2, f):
    l3 = f(l1, l2)
    node = l3
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)


l1 = ListNode(2, ListNode(5, ListNode(10)))
#l1 = None
l2 = ListNode(3, ListNode(4, ListNode(5, ListNode(7, ListNode(12)))))

#print(l1.val)
# Test 
test(l1,l2, mergeListIterative)
test(l1,l2, mergeListRecursively)



