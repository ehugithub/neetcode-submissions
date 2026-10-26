class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # solution space: k\in [1, max(piles)]
        # we can binary search this space to find the opt answer
        left, right = 1, max(piles)

        def canEat(k):
            time = 0
            for pile in piles:
                time += -(-pile // k)
            return time <= h
        print(canEat(1))

        while left <= right:
            mid = left + (right - left) // 2
            if canEat(mid):
                if not canEat(mid + 1):
                    return mid
                right = mid - 1
            else:
                left = mid + 1
        
        return mid if canEat(mid) else mid + 1
        