class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        res = 0

        for n in nums:
            s.add(n)

        for n in nums:
            if n - 1 not in s:
                count = 0
                while n in s:
                    count += 1
                    n += 1
                res = max(res, count)
        
        return res

        