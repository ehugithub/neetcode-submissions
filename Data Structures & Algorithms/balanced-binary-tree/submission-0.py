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

        q = deque([root])
        res = []

        while q:
            node = q.popleft()
            
            res.append(node)

            for child in [node.left, node.right]:
                if child: q.append(child)
        
        res.reverse()

        for node in res:
            heights[node] = max(heights[node.left], heights[node.right]) + 1

        
        for node in res:
            if abs(heights[node.left] - heights[node.right]) > 1: return False
        return True
        