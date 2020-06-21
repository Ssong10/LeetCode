# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
def nextval(tree, pre,sum):
    result = 0
    total = 0
    pre.append(tree.val)
    for p in reversed(pre):
        total += p
        if total == sum:
            result += 1
    if tree.left:
        result += nextval(tree.left,pre,sum)
    if tree.right:
        result += nextval(tree.right,pre,sum)
    pre.pop()
    return result

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:    
        if root:
            return nextval(root,deque([]),sum)
        else:
            return 0