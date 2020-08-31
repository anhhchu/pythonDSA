# Here is our Stack Class

class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()

class Queue:
    def __init__(self):
        # Code here
        self.ins = Stack()
        self.out = Stack()

    def size(self):
         # Code here
        return self.ins.size()+self.out.size()

    def enqueue(self,item):
        # Code here
        self.ins.push(item)

    def dequeue(self):
        # Code here
        if self.out.size() == 0:
            while self.ins.items:
                self.out.push(self.ins.pop())
        return self.out.pop()


queue = Queue()
queue.enqueue(5)
print(queue.ins.items, queue.out.items)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(15)
print(queue.dequeue())
print(queue.ins.items, queue.out.items)
print(queue.dequeue())
print(queue.ins.items, queue.out.items)
print(queue.dequeue())
print(queue.ins.items, queue.out.items)
print(queue.dequeue())
print(queue.ins.items, queue.out.items)
print(queue.dequeue())
print(queue.ins.items, queue.out.items)



