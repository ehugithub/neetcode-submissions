class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        res = 0
        chars = set()
        left = 0

        for right in range(n):
            ch = s[right]

            if ch not in chars:
                chars.add(ch)
                res = max(res, right - left + 1)
                
            else:
                while ch in chars:
                    l_ch = s[left]
                    chars.remove(l_ch)
                    left += 1
                chars.add(ch)

        return res





        