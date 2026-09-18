# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        n1 = l1
        n2 = l2

        dummy = ListNode()
        prev = dummy
        carry = 0

        while n1 or n2 or carry:
            add = carry
            if n1:
                add += n1.val
                n1 = n1.next
            if n2:
                add += n2.val
                n2 = n2.next
                
            node = ListNode(add % 10)
            carry = add // 10
            prev.next = node
            prev = node
 
        return dummy.next