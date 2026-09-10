# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        deque = collections.deque([root])
        res = []
        
        while deque:
            temp = []
            
            num = len(deque)

            for _ in range(num):
                node = deque.pop()
                temp.append(node.val)

                if node.left:
                    deque.appendleft(node.left)
                if node.right:
                    deque.appendleft(node.right)

            res.append(temp)


        return res

        