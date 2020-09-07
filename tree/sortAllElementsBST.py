'''
Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.

Example 1:
Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]

Example 2:
Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]

Example 3:
Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]

Example 4:
Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]

Example 5:
Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]
 

Constraints:

Each tree has at most 5000 nodes.
Each node's value is between [-10^5, 10^5].
'''


# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]

        inorder traversal of both tree 
        merge 2 sorted arrays
        O(N+M) (N, M number of nodes of each tree)
        """
        l1 = self.traverse(root1,[])
        l2 = self.traverse(root2, [])
        
        return self.merge(l1,l2)

    def traverse(self, node, visitOrder):
        if not node:
            return []

        if node.left:
            self.traverse(node.left, visitOrder)

        visitOrder.append(node.val)

        if node.right:
            self.traverse(node.right, visitOrder)

        return visitOrder
        
            


    def merge(self,l1, l2):
        
        i = j = 0
        arr = []
        while i < len(l1) and j < len(l2): 
            if l1[i] <= l2[j]:
                arr.append(l1[i])
                i += 1
            else:
                arr.append(l2[j])
                j += 1

        arr += l1[i:]
        arr += l2[j:]

        return arr
    
    

#print(merge([1, 2, 4],[0, 1, 3]))

