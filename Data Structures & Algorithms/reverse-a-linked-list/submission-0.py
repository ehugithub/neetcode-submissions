# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        cur = head
        cur2 = cur.next
        cur3 = cur2.next
        head.next = None

        while(cur2):
            cur2.next = cur
            cur = cur2
            cur2 = cur3
            if cur3:
                cur3 = cur3.next

        return cur
