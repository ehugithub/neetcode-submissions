# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q: return True

            p_q = deque([p])
            q_q = deque([q])

            while p_q and q_q:
                p_node = p_q.popleft()
                q_node = q_q.popleft()

                if (p_node is None) ^ (q_node is None): return False
                if (p_node is None) and (q_node is None): continue

                if p_node.val != q_node.val: return False

                for child in [p_node.left, p_node.right]:
                    p_q.append(child)
                for child in [q_node.left, q_node.right]:
                    q_q.append(child)

            return len(p_q) == len(q_q)

        q = deque([root])
        results = []

        while q:
            node = q.popleft()

            if node.val == subRoot.val:
                results.append(isSameTree(self, node, subRoot))

            for child in [node.left, node.right]:
                if child: q.append(child)

        return any(results)
        