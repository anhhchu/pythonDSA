'''
Given a node in a binary search tree, find the in-order successor of that node in the BST.

If that node has no in-order successor, return null.

The successor of a node is the node with the smallest key greater than node.val.

You will have direct access to the node but not to the root of the tree. Each node will have a reference to its parent node. Below is the definition for Node:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
 

Follow up:

Could you solve it without looking up any of the node's values?

 

Example 1:


Input: tree = [2,1,3], node = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both the node and the return value is of Node type.
Example 2:


Input: tree = [5,3,6,2,4,null,null,1], node = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
Example 3:


Input: tree = [15,6,18,3,7,17,20,2,4,null,13,null,null,null,null,null,null,null,null,9], node = 15
Output: 17
Example 4:


Input: tree = [15,6,18,3,7,17,20,2,4,null,13,null,null,null,null,null,null,null,null,9], node = 13
Output: 15
Example 5:

Input: tree = [0], node = 0
Output: null
 

Constraints:

-10^5 <= Node.val <= 10^5
1 <= Number of Nodes <= 10^4
All Nodes will have unique values.
'''



# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution(object):
    def inorderSuccessor(self, node):
        """
        :type node: Node
        :rtype: Node

        Time complexity : O(H) where HH is the height of the tree. That means O(logN) in the average case, and O(N) in the worst case, where N is the number of nodes in the tree.
        Space complexity : O(1), since no additional space is allocated during the calculation.
        """
        # if not parent -> node is root
            # if node has no right child-> return null
            # node has right child -> return the left most node of right child
            
        # if parent:
            # parent.val > node.val, node is left
                # node has no right child -> return parent.val
                # node has right child -> return the left most node of right child
            # parent.val < node.val, node is right
                # if node has right child ->  return the left most node of right child
                # traverse back to root, recursive call helper function to parent of node, each step compare temp with the new parent value. If found larger val -> return , else return None when hit root
        
        def helper_right(node):
            temp = node.right
            n = node.right
            while n.left:
                temp = n.left
                n = n.left
            return temp
            
        def helper_parent(node):
            while node.parent:
                if node.parent.val > node.val:
                    return node.parent
                else: 
                    node = node.parent
            
        if not node.parent:
            if not node.right:
                return None
            else:
                return helper_right(node)
            
        else:
            if node.parent.val > node.val: # node is left
                if not node.right:
                    return node.parent
                else:
                    return helper_right(node)
            else: # node is right
                if not node.right:
                    return helper_parent(node)
                else:
                    return helper_right(node)
    