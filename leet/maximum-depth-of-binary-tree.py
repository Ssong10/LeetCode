# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def find(depth,root):
    a , b = depth, depth
    if root.left:
        a = find(depth+1, root.left)
    if root.right:
        children = 1
        b = find(depth + 1,root.right)
    return max(a,b)

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            return find(1,root)
        else:
            return 0
    