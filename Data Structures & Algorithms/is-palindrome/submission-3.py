class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s.lower()))

        front = 0
        end = len(s) - 1

        while front < end:
            if s[front] != s[end]:
                return False
            front += 1
            end -= 1

        return True       