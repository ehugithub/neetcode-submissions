class Solution:
    def maxArea(self, height: list[int]) -> int:
        low = 0
        high = len(height) - 1
        res = 0

        while low < high:
            res = max(res, min(height[low], height[high]) * (high - low))
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1

        return res
        