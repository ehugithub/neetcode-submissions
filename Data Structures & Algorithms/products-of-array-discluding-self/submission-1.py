class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix prods
        prefix_prods = [1] * len(nums)
        suffix_prods = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix_prods[i] = nums[i - 1] * prefix_prods[i - 1]

        # suffix prods

        for i in range(len(nums) - 2, -1, -1):
            suffix_prods[i] = nums[i + 1] * suffix_prods[i + 1]
        

        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix_prods[i] * suffix_prods[i] 

        return res
        