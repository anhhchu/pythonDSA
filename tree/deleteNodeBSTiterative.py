# Definition for a binary tree node.
# Reference: https://leetcode.com/explore/featured/card/august-leetcoding-challenge/553/week-5-august-29th-august-31st/3443/discuss/822263/Python3-iterative-and-recursive

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root, key):
        # search for node
        node = root
        parent = left = None
        while node:
            if node.val < key: parent, node, left = node, node.right, False
            elif node.val > key: parent, node, left = node, node.left, True
            else: break # found 
        
        # delete the node 
        if node: # if found 
            # node has 1 child
            if not node.left or not node.right: 
                if parent: 
                    if left: parent.left = node.left or node.right
                    else: parent.right = node.left or node.right
                else: return node.left or node.right
            
            # node has 2 children
            else: 
                temp = parent = node
                node = node.left 
                if not node.right: parent.left = node.left
                else: 
                    while node.right: parent, node = node, node.right
                    parent.right = node.left
                temp.val = node.val
        return root 

def printTree(treeNode):
    node = treeNode
    if node:
        print(node.val)
        printTree(node.left)
        printTree(node.right)

def reconstructTree(arr):
    '''
    reconstruct tree from level array
    child index = 2*p + 1 or 2*p + 2
    '''
    if len(arr) <= 0:
        node = None
    
    node = TreeNode(arr[0])
    return _reconstructTree(arr, node, 0)

def _reconstructTree(arr, parentNode, p):
    c1 = 2*p + 1
    c2 = 2*p + 2
    if c1 < len(arr):
        parentNode.left = TreeNode(arr[c1])
        _reconstructTree(arr, parentNode.left, c1)
    if c2 < len(arr):
        parentNode.right = TreeNode(arr[c2])
        _reconstructTree(arr, parentNode.right, c2)
    return parentNode


arr = [5,3,6,2,4,None,7]
treeNode = reconstructTree(arr)
sol = Solution()

print('Delete 3')
sol.deleteNode(treeNode,3)
printTree(treeNode)

print('Delete 6')
sol.deleteNode(treeNode,6)
printTree(treeNode)

print('Delete 7')
sol.deleteNode(treeNode,7)
printTree(treeNode)