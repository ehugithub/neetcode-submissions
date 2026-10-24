class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            # o/w, run sorted two sum on remaining list
            # if found a match, need to check for multiple solutions after

            target = -num

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[left] + nums[right]
                if total > target:
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    res.append([-target, nums[left], nums[right]])
                    left += 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return res
        