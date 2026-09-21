class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals: return 0
        # sort first
        intervals.sort(key = lambda x: x[0])

        # want a greedy approach here  
        prevEnd = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < prevEnd:
                prevEnd = min(prevEnd, intervals[i][1])
                res += 1
            else:
                prevEnd = intervals[i][1]

        return res