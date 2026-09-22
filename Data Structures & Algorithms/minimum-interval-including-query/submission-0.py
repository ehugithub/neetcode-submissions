class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        res = [-1] * len(queries)
        sorted_queries = sorted([(ind, query) for ind, query in enumerate(queries)], key = lambda x: x[1])

        intervals.sort(key = lambda x: x[0])
        queries.sort()

        # heap of valid intervals, sorted by size
        valid_intervals = []

        curr_int = 0
        n = len(intervals)
        for ind, query in sorted_queries:
            while curr_int < n and intervals[curr_int][0] <= query:
                int_size = intervals[curr_int][1] - intervals[curr_int][0] + 1
                heapq.heappush(valid_intervals, (int_size, intervals[curr_int][1]))
                curr_int += 1
            
            while valid_intervals and valid_intervals[0][1] < query:
                heapq.heappop(valid_intervals)

            res[ind] = valid_intervals[0][0] if valid_intervals else -1
        return res
        