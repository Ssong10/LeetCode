# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode()
        tmp = l3
        while l1 or l2:
            print(tmp,l1,l2)
            if l1:
                tmp.val += l1.val
                l1 = l1.next
            if l2:
                tmp.val += l2.val
                l2 = l2.next
            if tmp.val >= 10:
                tmp.val -= 10
                tmp.next = ListNode(val=1)
            else:
                if l1 or l2:
                    tmp.next = ListNode()
            tmp = tmp.next
        return l3
        