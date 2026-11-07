# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0


        ptr = head
        while ptr:
            ptr = ptr.next
            length += 1

        n = length // k
        dummy = ListNode(next = head)
        ptr = dummy
        curr = head
        
        for _ in range(n):
            prevStart = ptr
            for _ in range(k):
                tmp = curr.next
                curr.next = ptr
                ptr = curr
                curr = tmp
            # dummy <-> 1 <- 2 <-  3    4 -> ...
            #                     ptr  curr

            prevStart.next.next = curr
            tmp = prevStart.next
            prevStart.next = ptr
            ptr = tmp

            # dummy -> 3 -> 2 -> 1 -> 4 -> ...
            #          ptr            curr

        return dummy.next

        
        