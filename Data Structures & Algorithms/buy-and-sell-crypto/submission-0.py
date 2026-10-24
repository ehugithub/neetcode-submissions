class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float('inf')
        res = 0

        for p in prices:
            lowest = min(lowest, p)
            res = max(res, p - lowest)

        return res
        