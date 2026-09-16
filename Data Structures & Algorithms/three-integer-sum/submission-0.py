class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            # skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # if positive, can't have triplets
            if nums[i] > 0:
                break
            
            # double pointer: two sum on sorted array with target = 0
            left, right = i + 1, n - 1
            while left < right:
                total = nums[left] + nums[right] + nums[i]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # skip duplicates:
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
            
        return res

        