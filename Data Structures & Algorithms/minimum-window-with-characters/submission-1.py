class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = Counter(t)
        left = 0
        res = ""
        res_len = float("inf")
        window_counts = {}
        have, need = 0, len(t_counts)

        for right in range(len(s)):
            ch = s[right]
            window_counts[ch] = window_counts.get(ch, 0) + 1
            if ch in t_counts and window_counts[ch] == t_counts[ch]:
                have += 1

            # if window contains all of t
            while have == need:
                if right - left + 1 < res_len:
                    res_len = right - left + 1
                    res = s[left : right + 1]

                left_ch = s[left]
                window_counts[left_ch] -= 1
                if left_ch in t_counts and window_counts[left_ch] < t_counts[left_ch]:
                    have -= 1
                if window_counts[left_ch] == 0:
                    del window_counts[left_ch]
                left += 1


        return res