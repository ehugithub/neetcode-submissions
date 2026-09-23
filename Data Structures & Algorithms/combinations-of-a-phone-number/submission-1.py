class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits: return []
        res = []
        path = ""
        n = len(digits)

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(ind):
            nonlocal path
            if len(path) == n or ind >= n:
                res.append(path)
                return
            
            for ch in phone[digits[ind]]:
                path += ch
                backtrack(ind + 1)
                path = path[:-1]

        backtrack(0)
        return res
        