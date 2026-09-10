# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # iterative version
        if not root: return 0

        # find height of every node
        heights = {None: 0}
        stack = [root]
        # keep track of traversal order
        order = []


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
            heights[node] = 1 + max(l_height, r_height)

        diam = 0
        for node in order:
            diam = max(diam, heights[node.left] + heights[node.right])

        return diam

            


