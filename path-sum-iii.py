# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
def nextval(tree, pre,sum):
    total = 0
    for p in reversed(pre):
        total += p
        if total == sum:
            result += 1
    if tree.left:
        pre.append(tree.left.val)
        nextval(tree.left,pre,sum)
        pre.pop()
    if tree.right:
        pre.append(tree.right.val)
        nextval(tree.right,pre,sum)
        pre.pop()

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        
        return nextval(root,deque([root.val]),sum)