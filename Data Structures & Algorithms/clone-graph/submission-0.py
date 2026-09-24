"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return node

        # orig nodes -> new nodes
        clones = {}

        def dfs(node):
            new_node = Node(node.val)
            if node in clones:
                return
            clones[node] = new_node

            for nbr in node.neighbors:
                dfs(nbr)

        dfs(node)

        for orig in clones:
            clones[orig].neighbors = [clones[nbr] for nbr in orig.neighbors]

        return clones[node]
        