'''
You have been provided a Python file, heap.py, which constructs a heap structure with a list. Using that code as a guide:

* Develop a heap data structure using a binary tree structure
* The heap must support add and remove from the heap
* All operations most abide by the rules that govern a heap

Once you have your heap structure created, next you must use it as a backing structure to a priority queue.
* Develop a priority queue data structure that is backed by the heap you just created
* Implement the normal methods that accompany a priority queue structure
* Enqueue, dequeue, and peek by priority not position
Also length and whether or not the structure is empty (is_empty)

Perform the following operations to showcase your working structure
* Enqueue the following items: 1-4, 7, 2-5, 11, 8, 6, 9
* Dequeue 3 items by priority, they should be 4, 5, & 6.
* Provide a basic interface to allow users to interact with the Priority Queue. 
This can be a simple CLI that provides the user with the basic options of "Enqueue", "Dequeue", etc.

     5
  7    6
11 8  9   
leaves = [(2,5), (7,11), (5,8)]
'''
from collections import deque

class TreeNode:
    def __init__(self,val=None):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        

class Heap(object): # use complete binary tree to build heap 
    def __init__(self):
        self.root = None
        self.leaves = deque()  # use deque to support popleft at O(1)
        self.count = 0
        
    def _get_leaves(self):  
        self.leaves = deque()
        q = deque([self.root])
        while q:
            node = q.popleft()
            if not node.left or not node.right:
                self.leaves.append(node) # leaves queue will keep a list of all nodes to attach new node to
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    
    def insert(self, key, value):
        
        # take the first node of the leaves queue self.leaves[0]
        # add the new node to the end of the leaves queue
        # add the new node to the left or right of the node self.leaves[0]
        self.count += 1
        if not self.root: 
            self.root = TreeNode((key,value))
            self._get_leaves()
            return 'Added First Node {value} with priority {key}'.format(value=value, key=key)

        node = self.leaves[0]
        self.leaves.append(TreeNode((key,value)))
        if not node.left: 
            node.left = self.leaves[-1] # reference to the same node in self.leaves
            
        elif not node.right:
            node.right = self.leaves[-1]
            self.leaves.popleft() # remove the node with 2 children out of leaves queue
        
        self.leaves[-1].parent = node

        # upheap process
        self._upheap(self.leaves[-1])

        return 'Added New Node {value} with priority {key}'.format(value=value, key=key)

    def bfs(self): # use this to test the heap
        if not self.root:
            return 'Empty Queue'
        q = deque([self.root])
        visit = []
        while q:
            node = q.popleft()
            #parent = node.parent.val if node.parent else None
            visit.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return visit
    
    @property
    def minchild(self):
        return self.root.val

    def pop(self):
        # check invalid tree
        if self.root is None:
            return "Nothing to Remove!!!"
        # copy the last node in self.leaves to root
        # delete leaf
        # downheap
        
        temp = self.leaves.pop()
        item = self.root.val
        self.count -= 1

        if temp == self.root: # the last node deleted is also root
            self.root = None
            return 'Deleted LAST node {item}'.format(item=item)
        elif temp.parent.right: 
            temp.parent.right = None
        else:
            temp.parent.left = None
        self.root.val = temp.val
        self._downheap(self.root)
        self._get_leaves()
        
        return 'Deleted node {item}'.format(item=item)

    def _upheap(self, node):
        if not node.parent: 
            return
        elif node.val[0] < node.parent.val[0]:
            node.val, node.parent.val = node.parent.val, node.val 
        self._upheap(node.parent)

    def _downheap(self, node):
        if not node.left and not node.right:
            return 
        smaller = node
        if node.left and node.left.val[0] < node.val[0]:
            smaller = node.left
        if node.right and smaller.val[0] > node.right.val[0]:
            smaller = node.right

        if smaller == node:
            return
        if smaller != node:
            node.val, smaller.val = smaller.val, node.val
            self._downheap(smaller)


class PQ(Heap):
    def __init__(self): 
        #Heap().__init__()
        super().__init__()
        
    def enqueue(self,k,v):
        return self.insert(k,v)
        #return  "Node with value {v} and priority {k} ADDED to queue".format(v=v, k=k)

    def peak(self):
        return self.minchild

    def dequeue(self):
        print([node.val for node in self.leaves])
        return self.pop()

    def size(self):
        return self.count

    def is_empty(self):
        return self.root is None

    def print_queue(self):
        return self.bfs()
    

def main():
    pq = PQ()
    #print(pq.add(1,6))
    #print(pq.add(2,7))
    #print(pq.remove_min())
    
    prompt = input("What do you want to do? Enter: 'e' to add, 'd' to remove top priority, 'm' to peak the min child, 'l' for length of queue, 'p' to print queue, 's' to leave: ")
        
    while prompt != 's':
        if prompt == 'e' :
            k, v = input('Enter key, value pair (e.g 1 2): ').split()
            print(pq.enqueue(k,v))
        elif prompt == 'd':
            print(pq.dequeue())
        elif prompt == 'm':
            print(pq.peak())
        elif prompt == 'l': 
            print(pq.size())
        elif prompt == 'p': 
            print(pq.print_queue())
        else: 
            print("Invalid Choice!!!")
        
        prompt = input("What do you want to do? Enter: 'e' to add, 'd' to remove top priority, 'm' to peak the min child, 'l' for length of queue, 'p' to print queue, 's' to leave: ")
             


main()
    
    


