class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = Counter(s1)
        window = {}
        left = 0
        n = len(s2)

        for right in range(n):
            ch = s2[right]
            window[ch] = window.get(ch, 0) + 1
            if window == s1_counts: return True 
            while left <= right and window.get(ch, 0) > s1_counts.get(ch, 0):
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1

        return False
        