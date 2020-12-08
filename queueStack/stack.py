class Node:
    '''Node object to store data and reference to next'''
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    '''Stack data structure that adhere to FILO philosphy'''
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        '''Put data onto the top of the stack'''
        node = Node(data)   # Make a new node with the data
        if self.top:    # If there are any items on the stack...
            node.next = self.top    # Set the next param to the top of the stack
            self.top = node     # Set the top of the stack to the new node
        else:
            self.top = node # Make the top of the stack the new node
        self.size += 1  # Increase the size of the stack
    
    def pop(self):
        if self.top:    # If the stack is not empty
            data = self.top.data # Get the data off the top
            self.top = self.top.next if self.top.next else None # Set the top to next node down
            self.size -= 1  # Decrease the stack size 
            return data
        return None # Return nothing if stack is empty
    
    def peek(self): 
        if self.top:    # If the stack isn't empty
            return self.top.data    # Return the top of the stack
        return None     # Else return nothing
    
    def flush(self):
        self.top = None # Set the top of the stack to nothing
        self.size = 0   # Set the size to 0