# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder: [root, left subtree, right subtree]
        # inorder: [left subtree, root, right subtree]

        # value -> its index in inorder
        indices = {val: ind for ind, val in enumerate(inorder)}
        self.pre_ind = 0

        def build(in_left, in_right):
            if in_left > in_right:
                return None

            # root node
            root_val = preorder[self.pre_ind]
            root_ind = indices[root_val]

            self.pre_ind += 1
            root = TreeNode(root_val)
            root.left = build(in_left, root_ind - 1)
            root.right = build(root_ind + 1, in_right)
            return root

        return build(0, len(inorder) - 1)

