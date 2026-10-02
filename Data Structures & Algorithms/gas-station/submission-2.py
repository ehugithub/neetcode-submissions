class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res = total = 0
        n = len(gas)
        ans = 0

        for i in range(n):
            diff = gas[i] - cost[i]
            res += diff
            total += diff

            if res < 0:
                ans = i + 1
                res = 0

        return ans if total >= 0 else -1

        