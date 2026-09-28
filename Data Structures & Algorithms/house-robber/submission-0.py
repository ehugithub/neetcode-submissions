class Solution:
    def rob(self, nums: List[int]) -> int:
        res = 0
        dp = [0] * (len(nums) + 1)


        for i, num in enumerate(nums):
            dp[i + 1] = max(dp[i], dp[i - 1] + nums[i])

        return dp[len(nums)]
        