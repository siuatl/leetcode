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
            isSameTree(p.left, q.left) and \
            isSameTree(p.right, q.right)
    else:
        return p == None and q == None


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
print(isSameTree(root, root2))


root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.right = TreeNode(1)

root4 = TreeNode(1)
root4.left = TreeNode(1)
root4.right = TreeNode(2)
print(isSameTree(root3, root4))

root5 = TreeNode(1)
root5.left = TreeNode(2)

root6 = TreeNode(1)
root6.right = TreeNode(2)
print(isSameTree(root5, root6))

root7 = TreeNode()

root8 = TreeNode()
print(isSameTree(root7, root8))

root9 = TreeNode(1)

root10 = TreeNode(1)
root10.right = TreeNode(2)
print(isSameTree(root9, root10))
