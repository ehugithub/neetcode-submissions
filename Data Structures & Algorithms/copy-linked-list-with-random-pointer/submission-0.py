"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        dummy = Node(x = 0)
        new_ptr = dummy
        ptr = head

        # maps each node to its clone
        d = defaultdict(Node)

        while ptr:
            tmp = Node(x = ptr.val)
            new_ptr.next = tmp
            d[ptr] = tmp 

            ptr = ptr.next
            new_ptr = new_ptr.next
        
        ptr = head
        while ptr:
            d[ptr].random = d[ptr.random] if ptr.random else ptr.random
            ptr = ptr.next

        return dummy.next