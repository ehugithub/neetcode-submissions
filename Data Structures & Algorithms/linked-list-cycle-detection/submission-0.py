# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        tortoise = head
        hare = head.next

        while hare:
            if tortoise == hare:
                return True
            tortoise = tortoise.next
            hare = hare.next
            if hare: hare = hare.next


        return False

        