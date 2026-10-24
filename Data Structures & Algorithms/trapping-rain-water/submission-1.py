class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)

        left, right = 0, n - 1
        l_max, r_max = height[left], height[right]

        while left < right:
            if l_max < r_max:
                left += 1
                l_max = max(l_max, height[left])
                res += max(l_max - height[left], 0)
            else:
                right -= 1
                r_max = max(r_max, height[right])
                res += max(r_max - height[right], 0)
        return res

        