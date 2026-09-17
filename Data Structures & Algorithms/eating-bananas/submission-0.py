class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # 1 <= k <= n
        # binary search over the sample space?
        isFeasible = False
        k = max(piles)

        left = 0
        right = max(piles)

        def isFeasible(num):
            if num == 0: return False
            res = 0
            for pile in piles:
                res += math.ceil(pile / num)
            return res <= h 

        mid = 0

        while left < right:
            mid = left + (right - left) // 2
            if not isFeasible(mid) and isFeasible(mid + 1): return mid + 1
            # check if mid is feasible
            if isFeasible(mid):
                right = mid
            else:
                left = mid + 1


        