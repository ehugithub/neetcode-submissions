class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        path = []

        def backtrack(ind, remaining):
            if remaining < 0 or ind >= len(candidates):
                return
            elif remaining == 0:
                res.append(path.copy())
                return

            path.append(candidates[ind])
            backtrack(ind, remaining - candidates[ind])
            path.pop()

            backtrack(ind + 1, remaining)
        backtrack(0, target)

        return res
        