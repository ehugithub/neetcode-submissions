class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        left = max_freq = res = 0

        n = len(s)
        for right in range(n):
            freq[s[right]] += 1
            max_freq = max(max_freq, freq[s[right]])

            window_len = right - left + 1

            if window_len - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res
        