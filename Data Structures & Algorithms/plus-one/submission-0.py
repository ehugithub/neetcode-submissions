class Solution:
    def plusOne(self, digits: List[int]) -> List[int]: 
        n = len(digits)

        def increment(ind):
            nonlocal digits
            if digits[ind] < 9:
                digits[ind] += 1
            else:
                if ind > 0:
                    digits[ind] = 0
                    increment(ind - 1)
                else:
                    digits = [1] + [0] * n

        increment(n - 1)
        return digits
