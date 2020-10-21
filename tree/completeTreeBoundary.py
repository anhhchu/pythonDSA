'''
provided a complete tree
return the boundary of the tree
all tree node values are characters

            a
    b               c
  d    e        f     g
h  i  j  k     l  m  n  o
  
return [a b d h i j k l m n o g c]
'''

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None

    def constructByArr(self, root, arr, p):
        '''
        reconstruct a complete tree from level array
        '''
        # left_child = 2*p+1, right_child = 2*p+2
        
        if p >= len(arr):
            return

        else:
            root = TreeNode(arr[p])
            left_child = 2*p+1 
            right_child = 2*p+2
            root.left = self.constructByArr(root, arr, left_child)
            root.right = self.constructByArr(root, arr, right_child)
            
            return root

    def preorder(self, root, visit):
        if root:
            visit.append(root.val)
            self.preorder(root.left, visit)
            self.preorder(root.right, visit)

    def postorder(self, root, visit):
        if root:
            self.postorder(root.left, visit)
            self.postorder(root.right, visit)
            visit.append(root.val)


arr = ['a','b','c','d','e','f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
#arr = ['a','b','c','d','e']
tree = Tree()
tree.root = tree.constructByArr(tree.root, arr,0)
#root = tree.root
#print(root.val, root.left.val, root.right.val, root.left.left.val, root.left.right.val, root.right.left.val, root.right.right.val)
visit = []
tree.preorder(tree.root, visit)    
print('preorder traversal', visit)
visit = []
tree.postorder(tree.root, visit)    
print('postorder traversal', visit)    

def treeBoundary(root):
    '''
    3 levels of traversal
    1) traverse left: keep the left nodes, only check the left children [a, b, d, h] -> pop h 
    2) traverse right: keep the right nodes, only check the right children [c, g, o] -> pop o and reverse the array 
    3) traverse bottom/leaf: level traversal, only keep the leaf values [h i j k l m n o]
    '''
    
    
    def leftTraverse(root, arr):
        if not root:
            return
        arr.append(root.val)
        leftTraverse(root.left, arr)

    def rightTraverse(root, arr):
        if not root:
            return 
        arr.append(root.val)
        rightTraverse(root.right, arr)

    def bottomTraverse(root, arr):
        if not root:
            return 
        bottomTraverse(root.left, arr)
        if not root.left: # indicate leaf node
            arr.append(root.val)
        bottomTraverse(root.right, arr)

    left, right, bottom = [], [], []
    leftTraverse(root, left)
    left.pop()
    rightTraverse(root.right, right) # this will take care of the root
    right.pop()
    right = right[::-1]
    bottomTraverse(root, bottom)
    print('left', left)
    print('right', right)
    print('bottom', bottom)

    return left + bottom + right


print(treeBoundary(tree.root))



    
     
    
    