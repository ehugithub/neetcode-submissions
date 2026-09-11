class Solution:
    def plusOne(self, digits: List[int]) -> List[int]: 
        # iterative version:
        n = len(digits)

        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            if i > 0:
                digits[i] = 0
            else:
                return [1] + [0] * n

        return digits