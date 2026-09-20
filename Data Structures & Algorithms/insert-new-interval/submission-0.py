class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        before = []
        after = []
        newStart, newEnd = newInterval[0], newInterval[1]

        for interval in intervals:
            # starts and ends before
            if interval[1] < newStart:
                before.append(interval)
                continue
            elif interval[0] > newEnd:
                after.append(interval)
                continue
            # else: overlap
            newStart = min(newStart, interval[0])
            newEnd = max(newEnd, interval[1])
        
        return before + [[newStart, newEnd]] + after
        