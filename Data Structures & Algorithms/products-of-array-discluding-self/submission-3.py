class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        # calc the prefix
        prefix = 1
        for i in range(n):
            res[i] *= prefix
            prefix *= nums[i]

        # in reverse order, calc the suffix, skip the first ele
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
        