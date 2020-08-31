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
        root = None
    
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


arr = [5, 3, 6, 2, 4, None, 7]

tree = reconstructTree(arr)


def preOrderDfs(root):
    if root is None:
        return 
    visit_order = []
    return traverse(root, visit_order)

def traverse(node, visit_order):
    visit_order.append(node.val)
    if node.left:
        traverse(node.left, visit_order)
    if node.right:
        traverse(node.right, visit_order)
    return visit_order

visit_order = preOrderDfs(tree)
print(visit_order)


            
    

