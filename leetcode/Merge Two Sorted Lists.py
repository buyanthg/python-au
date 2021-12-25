class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = None
        if list1 and list2:
            if list1.val < list2.val:
                head = res = list1
                list1 = list1.next
            else:
                head = res = list2
                list2 = list2.next
        else:
            if list1:
                head = res = list1
            if list2:
                head = res = list2
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        while list1:
            head.next = list1
            head = head.next
            list1 = list1.next
        while list2:
            head.next = list2
            head = head.next
            list2 = list2.next
        return res