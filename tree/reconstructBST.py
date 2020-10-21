'''
it's enough to reconstruct a BST with preorder or postorder traversal list alone
O(N) time since we visit each node once, and O(N) to store the entire tree
Constructing from postorder is more efficient than preorder
'''

import time
class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderReconstruct(preorder):
    '''
    BST reconstruct from Preorder Traversal
    '''
    # base case
    start = time.time()
    # reverse preorder
    #preorder = preorder[::-1] # pop(0) will cause O(N^2) as array as to resize. Therefore reverse the preorder list before running helper 

    def helper(lower = float('-inf'), upper = float('inf')):
        if not preorder or (preorder[0] < lower or preorder[0] > upper): 
            return
        
        val = preorder.pop(0) 
        root = TreeNode(val)
        #print(val, lower, upper)
        root.left = helper(lower, val)
        root.right = helper(val, upper)
        return root 
    end = time.time()  
    print('preorder Construction Time:', end - start)
    return helper()

def postorderReconstruct(postorder):
    '''
    BST reconstruct from PostOrder Traversal
    '''
    start = time.time()
    def helper(lower = float('-inf'), upper = float('inf')):
        if not postorder or postorder[-1] < lower or postorder[-1] > upper:
            return
        val = postorder.pop()
        root = TreeNode(val)
        root.right = helper(val, upper)
        root.left = helper(lower, val)
        return root
    end = time.time()
    print('Postorder Construction Time:', end - start)
    return helper()

def preorderTraverse(root, visit):
    if root:
        visit.append(root.val)
        preorderTraverse(root.left,visit)
        preorderTraverse(root.right,visit)  
    return visit

def inorderTraverse(root, visit):
    if root:       
        preorderTraverse(root.left,visit)
        visit.append(root.val)
        preorderTraverse(root.right,visit)    
    return visit

def postorderTraverse(root, visit):
    if root:
        postorderTraverse(root.left, visit)
        postorderTraverse(root.right, visit)
        visit.append(root.val)
    return visit

preorder = [20,8,4,12,10,14,22,21,25]
root = preorderReconstruct(preorder)
print('preorder',  preorderTraverse(root, []))
print('inorder', inorderTraverse(root, []))
print('postorder', postorderTraverse(root, []))

postorder = [4, 10, 14, 12, 8, 21, 25, 22, 20]
root2 = postorderReconstruct(postorder)
print('preorder',  preorderTraverse(root2, []))
print('inorder', inorderTraverse(root2, []))
print('postorder', postorderTraverse(root2, []))