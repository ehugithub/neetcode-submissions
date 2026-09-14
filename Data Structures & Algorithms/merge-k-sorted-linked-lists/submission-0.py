# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # min heap storing (root.val, root)
        heap = [(root.val, i, root) for i, root in enumerate(lists) if root]
        heapq.heapify(heap)

        dummy = ListNode()
        cur = dummy

        while heap:
            val, i, node = heapq.heappop(heap)

            cur.next = ListNode(val)
            cur = cur.next 

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
        