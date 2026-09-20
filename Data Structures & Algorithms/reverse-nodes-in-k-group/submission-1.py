# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next or not k:
            return head

        # need the length
        length = 0
        nde = head
        while nde:
            length += 1
            nde = nde.next
        iterations = length // k

        dummy = ListNode()
        prev = dummy
        curr = head

        for _ in range(iterations):
            prevTail = prev
            # current head of the segment becomes the tail, and vice versa
            currHead = curr
            for _ in range(k):
                tmp = curr
                curr = curr.next
                tmp.next = prev
                prev = tmp
            currTail = prev
            prevTail.next = currTail
            currHead.next = curr
            prev = currHead

        return dummy.next 