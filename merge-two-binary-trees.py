# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def merge(t1,t2):
    if not t1:
        return t2
    if not t2:
        return t1
    t1.val += t2.val

    t1.left = merge(t1.left,t2.left)
    t1.right = merge(t1.right,t2.right)
    return t1

class Solution:    
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        t3 = merge(t1,t2)
        return t3