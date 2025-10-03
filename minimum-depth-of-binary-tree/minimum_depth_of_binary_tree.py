from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"N({self.val})"


def minDepth(root):
    work_queue = deque()
    work_queue.append((root, 1))
    while work_queue:
        print(work_queue)
        node, level = work_queue.popleft()

        if node == None:
            continue
        elif node.left == None and node.right == None:
            return level
        else:
            work_queue.append((node.left, level + 1))
            work_queue.append((node.right, level + 1))
    return 0


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(minDepth(root))

root = TreeNode(3)
root.left = TreeNode(9)
root.left.left = TreeNode(10)
root.left.right = TreeNode(10)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(minDepth(root))

root = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)
root.right.right.right.right = TreeNode(6)
print(minDepth(root))

print(minDepth(None))


# def minDepthHelper(root, level):
#     if root == None:
#         return 100001
#     elif root.left == None and root.right == None:
#         return level
#     else:
#         return min(minDepthHelper(root.left, level + 1),
#                    minDepthHelper(root.right, level + 1))


# def minDepth(root):
#     if root == None:
#         return 0
#     return minDepthHelper(root, 1)
