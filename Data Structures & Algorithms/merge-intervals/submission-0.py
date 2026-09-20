class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # store in a stack: iterate through intervals
        # if there's an overlap, pop, merge, then push back in

        # sort intervals first:
        intervals.sort(key = lambda x: x[0])
        stack = []

        for interval in intervals:
            if not stack:
                stack.append(interval) 
                continue
            # check for overlap
            if stack[-1][1] >= interval[0]:
                recent_interval = stack.pop()
                newEnd = max(recent_interval[1], interval[1])
                stack.append([recent_interval[0], newEnd])
            else:
                stack.append(interval)

        return stack
            
            
        