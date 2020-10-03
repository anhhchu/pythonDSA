'''
Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.
https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3453/
 

Example 1:



Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
 

Note:

The number of nodes in the tree is between 1 and 1000.
node.val is 0 or 1.
The answer will not exceed 2^31 - 1.
'''
class TreeNode:
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
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        sumBinary = 0
        stack = [(root,0)]
        
        while stack:
            root, curr = stack.pop()
            if root is not None:
                curr = (curr << 1) | root.val
                #print(curr)
                
                if root.left == None and root.right == None:
                    sumBinary += curr
                    #print(sumBinary)
                else:
                    stack.append((root.left,curr))
                    stack.append((root.right,curr))
                
        return sumBinary

sol = Solution()

arr = [1,0,1,0,1,0,1]
tree = reconstructTree(arr)
print(sol.sumRootToLeaf(tree))

arr = [1,1,0,0,1]
tree = reconstructTree(arr)
print(sol.sumRootToLeaf(tree))

arr = [1,1,0,1,None,0,None]
tree = reconstructTree(arr)
print(sol.sumRootToLeaf(tree))
