# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # recurrence: max(diam(children), depth children + 1)
        diam = 0


        def height(node):
            if not node: return 0
            nonlocal diam

            left_h = height(node.left)
            right_h = height(node.right)

            diam = max(left_h + right_h, diam)

            return max(left_h, right_h) + 1

        height(root)

        return diam
        