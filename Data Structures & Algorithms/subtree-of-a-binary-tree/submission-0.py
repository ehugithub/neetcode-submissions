# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            stack1 = [p]
            stack2 = [q]

            while stack1 and stack2:
                node1 = stack1.pop()
                node2 = stack2.pop() 

                if not node1 and not node2: continue
                elif not node1 or not node2: return False
                elif node1.val != node2.val: return False

                stack1.extend([node1.left, node1.right])
                stack2.extend([node2.left, node2.right])

            return True

        stack = [root]

        while stack:
            node = stack.pop()

            if isSameTree(node, subRoot): return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return False
        