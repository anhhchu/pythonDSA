# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

# [3,9,20,null,null,15,7]

#from collections import deque
class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return
        '''
        level, output, siblings = 0, [], []
        q = deque([(level,root)])
        while q:
            level, node = q.popleft() # level, node = 1,9, q = [(1,20)]
            siblings.append(node.val) # siblings = [9]
            
            if not q or (q and level != q[0][0]):
                if level % 2 != 0: # siblings at odd level will be reversed
                    siblings.reverse() 
                output.append(siblings)
                siblings = []
                
            level+=1
            if node.left:
                q.append((level,node.left))
            if node.right:
                q.append((level,node.right))
                
        return output
        '''
        
        q = [root]
        level = 0
        output = []
        while q: # reset siblings, next_level 
            siblings = []
            next_level = []
            level += 1
            for node in q: 
                siblings.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            if level % 2 == 0: # reverse
                output.append(siblings[::-1])
            else:
                output.append(siblings)
                
            q = next_level
            
        return output
            