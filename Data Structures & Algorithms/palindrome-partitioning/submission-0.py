class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def isPalindrome(s):
            return s == s[::-1]

        def backtrack(start):
            if start == len(s):
                res.append(list(path))

            for end in range(start, len(s)):
                candidate = s[start: end + 1]
                if isPalindrome(candidate):
                    path.append(s[start:end + 1])
                    backtrack(end + 1)
                    path.pop()
        backtrack(0)
        
        return res
        