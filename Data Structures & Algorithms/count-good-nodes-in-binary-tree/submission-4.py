# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # iteratively
        # we need to know the root value before going to left / right subtrees
        # so preorder is the correct dfs
        # also need to track the max value so far associated with each node as we traverse
        stack = [(root, root.val)]
        good_nodes = 0

        while stack:
            node, max_so_far = stack.pop()

            if node.val >= max_so_far:
                good_nodes += 1
            new_max = max(node.val, max_so_far)

            if node.left:
                stack.append((node.left, new_max))
            if node.right:
                stack.append((node.right, new_max))

        return good_nodes
            


        