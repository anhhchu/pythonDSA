class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,value):
        if self.head is None:
            self.head = Node(value)
            return
        #node.next = self.head
        #self.head = node

        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def repr(self):
        return str([v for v in self])


ll = LinkedList()

for value in [1,2,3,4,5]:
    ll.append(value)

for v in ll.__iter__():
    print(v)
print(ll.repr())


def reverse(linkedlist):
    list = []
    for v in linkedlist.__iter__():
        list.append(v)
    ll = LinkedList()
    while list:
        ll.append(list.pop())

    print(ll.repr())
    return ll

flipped = reverse(ll)
print(list(flipped))
print(list(ll) == list(reverse(flipped)))

llist = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist.append(value)

flipped = reverse(llist)
is_correct = list(flipped) == list([0,-3,1,5,2,4]) and list(llist) == list(reverse(flipped))
print("Pass" if is_correct else "Fail")

def reverse_sol(linkedlist):
    new_llist = LinkedList()
    prev_node = None

    for value in linkedlist:
        print(value)
        node = Node(value)

        node.next = prev_node
        prev_node = node
        print('prev node value', prev_node.value)

    new_llist.head = prev_node
    return new_llist

llist2 = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist2.append(value)

flipped_sol = reverse_sol(llist2)
print(flipped_sol.repr())
is_correct = list(flipped_sol) == list([0,-3,1,5,2,4]) and list(llist2) == list(reverse_sol(flipped_sol))
print("Pass" if is_correct else "Fail")
