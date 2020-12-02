'''
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
 

Constraints:

The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000
'''


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        '''
        level = 0
        q = deque([[level,root]])
        
        while q:
            level, node = q.popleft()
            if q and level == q[0][0]:
                node.next = q[0][1]
            level += 1
            if node.left:
                q.append([level, node.left])
            if node.right:
                q.append([level, node.right])
                
        return root
        '''
    
        def connect(node):
            while node and node.left: # 7,14
                if node.next: # 
                    node.left.next = node.right # 10 -> 11
                    node.right.next = node.next.left  # 11 -> 12
                    node = node.next  # 6
                else:
                    node.left.next = node.right # 14 -> 15
                    break
        
        if root.left: 
            root.left.next = root.right # 2->3
         
        node = root.left # 2
        while node: # 4
            connect(node) 
            node = node.left
        #connect(root.right)
        
        return root
                
            