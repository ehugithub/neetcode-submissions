class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, path):
            if i == len(nums):
                res.append(path.copy())
                return

            # choose not to include nums[i]
            backtrack(i + 1, path)

            # choose to include nums[i]
            path.append(nums[i])
            backtrack(i + 1, path)
            # then, backtrack
            path.pop()
        backtrack(0, [])
        return res
        