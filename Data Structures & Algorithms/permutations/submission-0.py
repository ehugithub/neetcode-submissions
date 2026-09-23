class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        path = []

        def backtrack(options):
            if not options:
                res.append(path.copy())
                return

            for i in range(len(options)):
                path.append(options[i])
                backtrack([num for num in options if num != options[i]])
                path.pop()
              
        backtrack(nums)
            
        return res
        