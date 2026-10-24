class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = Counter(t)
        res = ""
        have = left = 0
        min_len = float('inf')
        win_counts = defaultdict(int)

        need = len(t_counts.keys())


        for right in range(len(s)):
            ch = s[right]
            win_counts[ch] += 1

            if win_counts[ch] == t_counts[ch]:
                have += 1

            while have == need:
                substr = s[left: right + 1]
                if len(substr) < min_len:
                    min_len = len(substr)
                    res = substr
                    
                l_ch = s[left]
                win_counts[l_ch] -= 1
                if win_counts[l_ch] < t_counts[l_ch]:
                    have -= 1
                left += 1
        
        return res
        