# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def printTree(treeNode):
    node = treeNode
    if node:
        print(node.val)
        printTree(node.left)
        printTree(node.right)


class Solution:
    def deleteNode(self, root, key):

        # empty tree
        if not root:
            return root

        elif key < root.val:
           root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        else:
            
            if not root.left:
                temp = root.right
                root = None
                return temp 

            elif not root.right:
                temp = root.left
                root = None
                return temp

            else: 
                temp = self._findMin(root.right)
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)

        return root
    
    def _findMin(self, root):
        node = root
        while node.left:
            node = node.left
        return node


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







        