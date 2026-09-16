class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)

        left_max = right_max = 0
        left = 0
        right = n - 1

        res = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if height[left] < height[right]:
                res += max(0, left_max - height[left + 1])
                left += 1
            else:
                res += max(0, right_max - height[right - 1])
                right -= 1

        return res
        