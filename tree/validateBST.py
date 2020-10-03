'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / 
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / 
  1   4
     / 
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        O(N) time and space: number of nodes in tree, space for the call stack
        
        """
        # recursively check each subtree with helper function
        # for each recursion, 
            #keep track of the upper and lower bound of each node value
        
        #base case: tree is empty or node value is not in bound
        
        def helper(node, upper = float('inf'), lower = float('-inf')):
            
            
            if node is None:
                return True
            
            if node.val <= lower or node.val >= upper: 
                return False
            
            if not helper(node.left, node.val, lower):
                return False
            if not helper(node.right, upper, node.val):
                return False
            
            return True
        
        return helper(root)