# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        ptr = dummy
        carry = 0

        while l1 or l2 or carry > 0:
            total = carry
            if l1:
                total += l1.val
            if l2:
                total += l2.val
            tmp = ListNode(val = total % 10)
            carry = total // 10
            ptr.next = tmp
            ptr = tmp
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
        