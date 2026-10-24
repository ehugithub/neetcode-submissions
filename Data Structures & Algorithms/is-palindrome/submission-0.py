class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(ch for ch in s if ch.isalnum()).lower()

        return cleaned == cleaned[::-1]        