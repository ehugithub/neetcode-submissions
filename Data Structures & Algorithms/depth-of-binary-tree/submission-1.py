# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        # need to track how far each node is from the root
        distances = {root: 1}

        stack = [root]

        while stack:
            node = stack.pop()

            if node.left:
                distances[node.left] = distances[node] + 1
                stack.append(node.left)
            if node.right:
                distances[node.right] = distances[node] + 1
                stack.append(node.right)

        return max(distances.values())






        