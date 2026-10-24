class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = Counter(s1)
        left = 0
        d = defaultdict(int)

        for right in range(len(s2)):
            ch = s2[right]
            d[ch] += 1
            
            win_size = right - left + 1
            if win_size > len(s1):
                l_ch = s2[left]
                d[l_ch] -= 1
                if d[l_ch] == 0:
                    del d[l_ch]
                left += 1

            if d == s1_counts:
                return True

        return False
        