# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepthHelper(root, level):
    if root != None:
        return max(maxDepthHelper(root.left, level + 1),
                   maxDepthHelper(root.right, level + 1))
    else:
        return level - 1


def maxDepth(root):
    return maxDepthHelper(root, 1)


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(maxDepth(root))


root = TreeNode(1)
root.right = TreeNode(2)
print(maxDepth(root))

# root = TreeNode(None)
print(maxDepth(None))
