class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        curr_str = ""

        def backtrack(num_open, num_close):
            nonlocal curr_str
            # note: num_close <= num_open always
            if num_close == n:
                res.append(curr_str)
                return
            
            if num_open < n:
                curr_str += '('
                backtrack(num_open + 1, num_close)
                curr_str = curr_str[:-1]
            
            if num_close < num_open:
                curr_str += ')'
                backtrack(num_open, num_close + 1)
                curr_str = curr_str[:-1]
        backtrack(0, 0)
        return res
        