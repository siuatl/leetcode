# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversalHelper(root, order):
    if root != None:
        order.append(root.val)
        preorderTraversalHelper(root.left, order)
        preorderTraversalHelper(root.right, order)


def preorderTraversal(root):
    lis_order = []
    preorderTraversalHelper(root, lis_order)
    return lis_order


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(preorderTraversal(root))


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(7)
root.right.right.left = TreeNode(9)
print(preorderTraversal(root))
