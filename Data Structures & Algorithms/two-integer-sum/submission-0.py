class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums -> indices
        d = {}

        for id, num in enumerate(nums):
            if target - num in d:
                return [d[target - num], id]
            else:
                d[num] = id
        