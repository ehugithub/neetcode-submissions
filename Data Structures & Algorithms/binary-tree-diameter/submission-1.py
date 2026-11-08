# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # recurrence: max(diam(children), depth children + 1)
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

        q = deque([root])
        diam = 0

        while q:
            print(diam)
            node = q.popleft()

            left_h = heights[node.left] if node.left else 0
            right_h = heights[node.right] if node.right else 0

            diam = max(diam, left_h + right_h)

            for child in [node.left, node.right]:
                if child:
                    q.append(child)

        return diam


