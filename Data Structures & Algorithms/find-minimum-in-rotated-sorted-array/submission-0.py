class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        while left < right:
            mid = left + (right - left) // 2
            print(f"{nums[left]} {nums[mid]} {nums[right]}")
            if (nums[left] >= nums[mid] and nums[mid] >= nums[right]) or (nums[left] <= nums[mid] and nums[mid] >= nums[right]):
                left = mid + 1
            else:
                right = mid
        return nums[left]
        
        