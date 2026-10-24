class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = maxfreq = left = 0
        counts = defaultdict(int)

        for right in range(len(s)):
            ch = s[right]
            counts[ch] += 1
            maxfreq = max(maxfreq, counts[ch])

            win_size = right - left + 1
            # check if window is valid
            # if not, shrink from the left
            while win_size > maxfreq + k:
                l_ch = s[left]
                counts[l_ch] -= 1
                maxfreq = max(counts.values())
                win_size -= 1
                left += 1
            
            res = max(res, win_size)


        return res
        