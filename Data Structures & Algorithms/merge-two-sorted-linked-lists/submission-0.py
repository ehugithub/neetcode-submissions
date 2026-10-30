# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2: return list1
        if not list1: return list2
        if not list2: return list1

        dummy = ListNode()
        ptr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tmp = ListNode(list1.val)
                ptr.next = tmp
                list1 = list1.next
            else:
                tmp = ListNode(list2.val)
                ptr.next = tmp
                list2 = list2.next
            
            ptr = ptr.next


        if list1:
            ptr.next = list1
        elif list2:
            ptr.next = list2

        return dummy.next

        