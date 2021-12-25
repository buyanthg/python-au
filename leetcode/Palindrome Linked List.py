class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tail = None
        while head:
            head.next, tail, head = tail, head, head.next
        return tail

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

    def isPalindrome(self, head):
        mid = self.middleNode(head)
        back = self.reverseList(mid)
        while back != None:
            if head.val != back.val:
                return False
            head, back = head.next, back.next

        return True
