'''
https://leetcode.com/problems/diameter-of-binary-tree/
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / 
        2   3
       /      
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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


class Solution(object):
    def diameterOfBinaryTree(self, root):
        '''
        Time O(N^2) each node is touched twice for height and diameter calculation
        '''
        # remember: base case is when tree is empty, return 0
        if root is None:
            return 0
        
        # calculate height of each subtree
        heightL = self.height(root.left)
        heightR = self.height(root.right)
        
        # recursively calculate diameter at each node of the tree and return the max
        return max(heightL+heightR, max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right)))
        
        
        # use a helper function to calculate height
    def height(self, root):
        # base case
        if root is None:
            return 0
        
        # calculate height for each subtree and get the max 
        return 1 + max(self.height(root.left), self.height(root.right))
        
sol = Solution()
arr = [1,2,3,4,5]
tree = reconstructTree(arr)
print(sol.diameterOfBinaryTree(tree))




