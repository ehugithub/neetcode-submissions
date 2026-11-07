# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # maintain a min heap as we process through each sorted list
        # need another identifier (i.e index) so we can map each value to their linked list
        dummy = ListNode()
        ptr = dummy

        heap = [(head.val, ind) for ind, head in enumerate(lists) if head]
        heapq.heapify(heap)

        while heap:
            v, i = heapq.heappop(heap)
            tmp = ListNode(val = v)
            ptr.next = tmp
            ptr = tmp

            if lists[i].next:
                lists[i] = lists[i].next
                heapq.heappush(heap, (lists[i].val, i))

        return dummy.next

        