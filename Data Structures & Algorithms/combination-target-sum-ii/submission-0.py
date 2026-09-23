class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        path = []
        candidates.sort()

        def backtrack(ind, remaining):
            if remaining == 0:
                res.append(path.copy())
                return
            
            for i in range(ind, len(candidates)):
                if candidates[i] > remaining:
                    break
                if i > ind and candidates[i] == candidates[i - 1]:
                    continue 
                path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i])
                path.pop()

        backtrack(0, target)
        return res
        