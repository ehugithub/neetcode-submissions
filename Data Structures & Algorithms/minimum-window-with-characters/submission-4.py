class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = Counter(t)
        d = {}
        have, need = 0, len(t_counts)
        left = 0

        res = ""
        res_len = float("inf")

        for right in range(len(s)):
            ch = s[right]
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1

            if ch in t_counts and d[ch] == t_counts[ch]:
                have += 1

            while have == need:
                if right - left + 1 < res_len:
                    res_len = right - left + 1
                    res = s[left : right + 1]

                left_ch = s[left]
                d[left_ch] -= 1
                if left_ch in t_counts and d[left_ch] < t_counts[left_ch]:
                    have -= 1
                if d[left_ch] == 0:
                    del d[left_ch]

                left += 1
        return res
