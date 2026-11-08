# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        q = deque([root])
        res = []

        while q:
            l = len(q)

            level = []
            for _ in range(l):
                node = q.popleft()
                level.append(node.val)

                for child in [node.right, node.left]:
                    if child: q.append(child)
            res.append(level)

        return [l[0] for l in res]

        