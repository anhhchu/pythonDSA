# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root, key):
        node = root
        if node.val:
            return
        elif node.val == key and not (node.left and node.right):
            node = None


sol = Solution()

        