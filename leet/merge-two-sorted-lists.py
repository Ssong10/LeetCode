# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(val='')
        tmp = l3
        while l1 or l2:
            if not l1:
                tmp.val = l2.val
                l2 = l2.next
            elif not l2:
                tmp.val = l1.val
                l1 = l1.next
            else:
                if l1.val <= l2.val:
                    tmp.val = l1.val
                    l1 = l1.next
                else:
                    tmp.val = l2.val
                    l2 = l2.next
            if l1 or l2:
                tmp.next = ListNode()
                tmp = tmp.next
        return l3
