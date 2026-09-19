class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        in_idx = 0

        for i in range(1, len(preorder)):
            val = preorder[i]
            node = TreeNode(val)
            last = None

            # pop while top of stack matches current inorder position —
            # means that subtree (and its left side) is fully built,
            # so this new value must be a RIGHT child of some ancestor
            while stack and stack[-1].val == inorder[in_idx]:
                last = stack.pop()
                in_idx += 1

            if last:
                last.right = node
            else:
                stack[-1].left = node

            stack.append(node)

        return root