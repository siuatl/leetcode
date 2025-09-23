# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p, q):
    if p != None and q != None:
        return  \
            (p.val == q.val) and \
            isSameTree(p.left, q.right) and \
            isSameTree(p.right, q.left)
    else:
        return p == None and q == None


def isSymmetric(root):
    return isSameTree(root, root)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.left = TreeNode(4)
root.left.right = TreeNode(4)
root.right.right = TreeNode(3)

print(isSymmetric(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.right = TreeNode(3)
root.right.right = TreeNode(3)

print(isSymmetric(root))
