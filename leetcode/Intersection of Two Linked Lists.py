class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def linked_list_len(self, head):
        i = 0
        while head:
            head = head.next
            i += 1
        return i
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA, lenB = self.linked_list_len(headA), self.linked_list_len(headB)
        while lenA > lenB:
            lenA -= 1
            headA = headA.next
        while lenA < lenB:
            lenB -= 1
            headB = headB.next
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None