# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def inorderTraversalHelper(root, results):
#     # WITH RECURSION
#     if root != None:
#         inorderTraversalHelper(root.left, results)
#         results.append(root.val)
#         inorderTraversalHelper(root.right, results)


# def inorderTraversal2(root):
#     lis = []
#     inorderTraversalHelper(root, lis)
#     return lis

def inorderTraversal(root):
    # WITH A LOOP
    results = []
    stack = []
    node = root
    while node != None or stack:
        if node != None:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            results.append(node.val)
            node = node.right
    return results


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print(inorderTraversal(root))


root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.left.right.left = TreeNode(6)
root2.left.right.right = TreeNode(7)
root2.right.right = TreeNode(8)
root2.right.right.left = TreeNode(9)


print(inorderTraversal(root2))
