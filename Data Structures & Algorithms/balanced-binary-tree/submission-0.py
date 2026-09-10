# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        heights = {None: 0}
        order = []
        stack = [root]

        while stack:
            node = stack.pop()
            order.append(node)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        order.reverse()

        for node in order:
            l_height = heights[node.left]
            r_height = heights[node.right]

            if abs(l_height - r_height) > 1: return False
            heights[node] = 1 + max(l_height, r_height)
            
        return True