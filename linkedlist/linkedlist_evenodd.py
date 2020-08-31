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

        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def __repr__(self):
        return ([v for v in self])

    def __iter__(self):
        if self.head is None:
            return None
        node = self.head
        while node:
            yield node.value
            node = node.next

def even_after_odd(linkedlist):
    if linkedlist.head
    even = linkedlist.head

