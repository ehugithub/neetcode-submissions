class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float("-inf")
        curr_max = 1
        curr_min = 1

        for num in nums:
            old_max = curr_max
            old_min = curr_min

            curr_max = max(num, old_max * num, old_min * num)
            curr_min = min(num, old_max * num, old_min * num)

            res = max(res, curr_max, curr_min)

        return res
        