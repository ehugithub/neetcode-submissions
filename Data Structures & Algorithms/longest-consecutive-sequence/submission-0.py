class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        res = 1

        s = set()

        for num in nums:
            if num not in s:
                s.add(num)
        
        for num in s:
            # if num - 1 not in s, it is the beginning of a sequence
            if num - 1 not in s:
                end = num
                # count how long this sequence is
                while end in s:
                    end += 1
                length = end - num
                res = max(res, length)

        return res
        