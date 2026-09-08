class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums) - 1
        low = 0

        while low < high:
            mid = low + (high - low + 1) // 2

            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] == target:
                return mid
            else:
                low = mid

        if nums[low] == target: return low

        return -1
        