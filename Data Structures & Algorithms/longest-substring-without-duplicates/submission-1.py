class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if not s: return 0
        # chars -> indices
        seen = {}
        
        res = 1
        left = 0

        for right in range(n):
            ch = s[right]
            if ch in seen and seen[ch] >= left:
                left = seen[ch] + 1

            res = max(res, right - left + 1)
            seen[ch] = right

        return res
        