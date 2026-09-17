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

        if not head: return None

        # maps old Nodes to new Nodes
        # Node -> Node
        d = {}
        node = head
        while node:
            d[node] = Node(node.val)
            node = node.next
        # match pointers
        node = head
        while node:
            d[node].next = d.get(node.next, None)
            d[node].random = d.get(node.random, None)
            node = node.next

        return d[head]
        