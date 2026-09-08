# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # recursive version
        diameter = 0

        def height(node):
            nonlocal diameter

            if not node: return 0

            left_h = height(node.left)
            right_h = height(node.right)

            diameter = max(diameter, left_h + right_h)
            return max(left_h, right_h) + 1

        height(root)
        return diameter
        