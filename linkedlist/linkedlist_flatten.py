class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    def __repr__(self):
        return str(self.value)

class LinkedList():
    def __init__(self):
        self.head = None

    def append(self,value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def __iter__(self):
        if self.head is None:
            return None
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        if self.head is None:
            return None
        node = self.head
        while node:
            return str([v for v in self])

def flatten(linkedlist):
    if linkedlist.head is None:
        return None
    node = linkedlist.head
    l = []
    while node:
        for val in node.value:
            l.append(val)
        node = node.next
    l.sort()
    ll = LinkedList()
    for val in l:
        ll.append(val)
    return ll

linkedlist1 = LinkedList()
for val in [0,2,4,6]:
    linkedlist1.append(val)
#print(linkedlist1.head.value)
print(linkedlist1.__repr__())

linkedlist2 = LinkedList()
for val in [1,3,5]:
    linkedlist2.append(val)

linkedlist = LinkedList()
linkedlist.append(linkedlist1)
linkedlist.append(linkedlist2)
print(linkedlist.__repr__())

flattened = flatten(linkedlist)
print(flattened.__repr__())

