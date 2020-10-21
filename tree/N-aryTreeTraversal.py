'''
Traverse an N-ary Tree 4 ways: preorder, postorder, inorder, level order
'''

class Solution:
    def preorderRecursion(self, root):
        
        def traverse(root, visit):
            if root: 
                visit.append(root.val)
                for child in root.children:
                    traverse(child, visit)
            return visit
        
        return traverse(root, [])
        
        
    def preorderIterative(self, root):
        stack = []
        if root: stack.append(root)
        visit = []
        while stack: # preorder: root, left, child
            node = stack.pop()
            visit.append(node.val)
            stack.extend(node.children[::-1])
                
        return visit