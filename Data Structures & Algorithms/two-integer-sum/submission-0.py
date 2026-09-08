class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for id, num in enumerate(nums):
            if target - num in d.keys():
                return [d[target - num], id]
            d[num] = id


        