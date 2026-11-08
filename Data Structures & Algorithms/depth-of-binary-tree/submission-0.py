# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        distances = {root: 1}

        q = deque([root])

        while q:
            node = q.popleft()

            for child in [node.left, node.right]:
                if child:
                    distances[child] = distances[node] + 1
                    q.append(child)


        return max(distances.values())
        