# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        curr = dummy = ListNode()
        l1, l2 = list1, list2
        while l1 or l2:
            if not l2:
                curr.next = l1
                l1 = l1.next
            elif not l1:
                curr.next = l2
                l2 = l2.next
            elif l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        return dummy.next
            

