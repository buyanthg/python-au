# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res, n = head, 0
        while head:
            n += 1
            head = head.next
            if n % 2 == 0:
                res = res.next
        return res