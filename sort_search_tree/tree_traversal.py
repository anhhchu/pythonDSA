class Node: 
        def __init__(self, data): 
            self.data = data 
            self.right_child = None 
            self.left_child = None 


def inorder(root_node,visit): 
        current = root_node 
        if current is None: 
            return 
        inorder(current.left_child,visit) 
        visit.append(current.data) 
        inorder(current.right_child,visit) 
        return visit

def preorder(root_node,visit): 
        current = root_node
        if current is None: 
            return 
        visit.append(current.data) 
        preorder(current.left_child,visit) 
        preorder(current.right_child,visit) 
        return visit


def postorder(root_node,visit): 
        current = root_node 
        if current is None: 
            return 
        postorder(current.left_child,visit) 
        postorder(current.right_child,visit) 
        visit.append(current.data)
        return visit


