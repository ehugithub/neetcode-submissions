class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for ind, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                (tmp, i) = stack.pop()
                res[i] = ind - i
            stack.append((temp, ind))

        return res
        