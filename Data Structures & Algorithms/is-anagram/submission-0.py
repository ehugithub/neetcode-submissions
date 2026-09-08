class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}

        for ch in s:
            d[ch] = d.get(ch, 0) + 1

        for ch in t:
            if ch in d.keys():
                if d[ch] == 0: return False
                d[ch] -= 1
            else:
                return False

        return all(val == 0 for val in d.values())
        