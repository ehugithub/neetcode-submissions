class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 1
        res = nums[0]

        for num in nums:
            if num == res:
                c += 1
            else:
                c -= 1
                if c == 0:
                    c = 1
                    res = num
        return res


        