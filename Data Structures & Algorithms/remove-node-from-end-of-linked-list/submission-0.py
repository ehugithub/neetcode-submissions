# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            l += 1

        ptr = head
        m = l - n + 1

        dummy = ListNode(next = head)
        ptr = dummy

        while m > 1:
            ptr = ptr.next
            m -= 1

        ptr.next = ptr.next.next

        return dummy.next
        