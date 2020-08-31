class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

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

    def is_circular(self):
        if self.head is None:
            return None
        fast = self.head
        slow = self.head
        while fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False

    def __repr__(self):
        if self.is_circular():
            print('Circular Node')
            return None
        return (str([v for v in self]))

list_with_loop = LinkedList()
for v in [0,4,3,2,1]:
    list_with_loop.append(v)

start_node = list_with_loop.head.next.next
node = list_with_loop.head
while node.next:
    node = node.next

node.next = start_node

print(list_with_loop.__repr__())

print(list_with_loop.is_circular())

ll = LinkedList()
for v in [0,4,3,2,1]:
    ll.append(v)

print(ll.__repr__())

print(ll.is_circular())
