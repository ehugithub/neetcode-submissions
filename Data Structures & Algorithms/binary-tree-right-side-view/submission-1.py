# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        # level-order traversal
        levels = []
        d = deque([root])
        while d:
            c = len(d)
            lev = []
            for _ in range(c):
                node = d.pop()
                lev.append(node.val)
                if node.right:
                    d.appendleft(node.right)
                if node.left:
                    d.appendleft(node.left)
            levels.append(lev)

        print(levels)

        return [level[0] for level in levels]

        