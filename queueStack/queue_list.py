class Queue:
    def __init__(self):
         # TODO: Initialize the Queue
        self.items = []

    def size(self):
         # TODO: Check the size of the Queue
        return len(self.items)

    def enqueue(self, item):
         # TODO: Enter item into Queue
        self.items.append(item)

    def dequeue(self):
         # TODO: Remove item from the Queue
        if self.size() == 0:
            return None
        return self.items.pop(0)


