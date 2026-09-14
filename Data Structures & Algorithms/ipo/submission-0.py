class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # two heaps:
        # heap 1: min heap sorted on capital
        # heap 2: max heap sorted on profit
        numCompleted = 0
        zipped = zip(profits, capital)

        tbd = [(cap, profit) for profit, cap in zipped]
        canDo = []
        heapq.heapify(tbd)

        while (tbd or canDo) and numCompleted < k:
            while tbd and tbd[0][0] <= w:
                cap, profit = heapq.heappop(tbd)
                heapq.heappush_max(canDo, (profit, cap))
            if canDo:
                profit, _ = heapq.heappop_max(canDo)
                w += profit
                numCompleted += 1
            else:
                break

        return w
        