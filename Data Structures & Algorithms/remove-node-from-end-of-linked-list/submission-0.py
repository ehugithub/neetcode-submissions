# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if not head.next: return None
        # find length
        length = 0

        node = head
        while node:
            length += 1
            node = node.next
        
        # if deleting the root:
        if length == n:
            return head.next

        count = length - n
        node = None
        nxt = head

        while count > 0:
            count -= 1
            node = nxt
            nxt = nxt.next

        # delete
        node.next = nxt.next

        return head
        