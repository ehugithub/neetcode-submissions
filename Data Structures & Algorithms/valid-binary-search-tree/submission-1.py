# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # in order traversal
        if not root: return True

        stack = []
        nums = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            nums.append(curr.val)
            curr = curr.right

        for i in range(len(nums) - 1):
            if nums[i + 1] <= nums[i]:
                return False 

        return True