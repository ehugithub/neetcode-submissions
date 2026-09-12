class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # quicksort
        if len(nums) < 2: return nums
        pivot = nums[len(nums) // 2]

        left = [x for x in nums if x < pivot]
        middle = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]
        
        return self.sortArray(left) + middle + self.sortArray(right)
        